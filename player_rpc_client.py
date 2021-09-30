import pika
import uuid
from config import rabbitMQHostname, rabbitMQPassword, rabbitMQUsername
from remote_server_utils import check_on_hogwarts


class PlayerRPCClient:
    def __init__(self):
        if check_on_hogwarts():
            credentials = pika.PlainCredentials(rabbitMQUsername, rabbitMQPassword)
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitMQHostname, credentials=credentials))
        else:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitMQHostname))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            self.response = body

    """
    A method to make calls to the player data API with GraphQL
    
    Example Payload:
    payload = {
        "query": "query($name: String!) { player(name: $name) { uuid }}",
        "variables": {"name": "KallumJ"} # VARIABLES IS REQUIRED, EVEN IF EMPTY
    }"""
    def call(self, payload):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="player-api",
            routing_key="",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.correlation_id
            ),
            body=payload
        )
        while self.response is None:
            self.connection.process_data_events()
        return self.response