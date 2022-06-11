from api.rpc_client import RPCClient
from config import rabbitMQRemoteHostname
from pika.exceptions import AMQPConnectionError
import logging;


class ServerRPCClient(RPCClient):
    def __init__(self):
        self.connected = True

        try:
            super().__init__(rabbitMQRemoteHostname, "server-api")
        except AMQPConnectionError:
            self.connected = False
            logging.warning("Unable to connect to the Server API. Is it running?")
