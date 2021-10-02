from rpc_client import RPCClient
from config import rabbitMQRemoteHostname


class PlayerRPCClient(RPCClient):
    def __init__(self):
        super().__init__(rabbitMQRemoteHostname, "player-api")
