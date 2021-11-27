from rpc_client import RPCClient
from config import rabbitMQRemoteHostname

from pika.exceptions import AMQPConnectionError


class PlayerRPCClient(RPCClient):
    def __init__(self):
        try:
            super().__init__(rabbitMQRemoteHostname, "player-api")
        except AMQPConnectionError:
            raise ConnectionError("Unable to connect to the Player API. Is it running?")
