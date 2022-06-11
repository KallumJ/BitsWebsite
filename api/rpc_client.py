import pika
from pika.exceptions import AMQPConnectionError

from config import rabbitMQPassword, rabbitMQUsername, rabbitMQLocalHostname
from util.remote_server_utils import check_on_hogwarts
import uuid

# I changed the way this client works, so it's now slightly different than the
# example. Instead of keeping our consumer open at all times, we close it as soon
# as we've received the reply from the server, and start consuming again the next
# time we want to send a query. I also added some extra checks to make sure we
# reconnect if the connection is ever lost. - Nex


class RPCClient:
    def __init__(self, hostname, exchange):
        self.exchange = exchange
        self.hostname = hostname
        self.connection = None
        self.connect()

    def connect(self):
        # if the connection is already open, don't do anything
        if self.connection is not None and self.connection.is_open:
            return

        if check_on_hogwarts():
            credentials = pika.PlainCredentials(rabbitMQUsername, rabbitMQPassword)
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.hostname, credentials=credentials))
        else:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitMQLocalHostname))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

    def on_response(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            # store the response
            self.response = body
            # stop consuming on the reply queue
            self.channel.basic_cancel(self.consumer_tag)

    """
    A method to make calls to the API with GraphQL

    Example Payload:
    payload = {
        "query": "query($name: String!) { player(name: $name) { uuid }}",
        "variables": {"name": "KallumJ"} # VARIABLES IS REQUIRED, EVEN IF EMPTY
    }
    """
    def call(self, payload):
        # if we don't have a connection, open a connection first
        if not self.connection.is_open:
            print("Connection lost, reconnecting")
            self.connect()

        try:
            # clear the response and generate a new correlation ID
            self.response = None
            self.correlation_id = str(uuid.uuid4())

            # we start consuming on our reply queue
            self.consumer_tag = self.channel.basic_consume(
                queue=self.callback_queue,
                on_message_callback=self.on_response,
                auto_ack=True
            )

            # publish the query to the server
            self.channel.basic_publish(
                exchange=self.exchange,
                routing_key="",
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.correlation_id
                ),
                body=payload
            )

            # wait for a response
            while self.response is None:
                self.connection.process_data_events()
            return self.response

        except AMQPConnectionError:
            print("Connection lost, reconnecting")
            self.connect()
            return self.call(payload)
