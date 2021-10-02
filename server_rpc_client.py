from rpc_client import RPCClient
from config import rabbitMQRemoteHostname


class ServerRPCClient(RPCClient):
    def __init__(self):
        super().__init__(rabbitMQRemoteHostname, "server-api")
