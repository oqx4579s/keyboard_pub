import os

import zmq
import zmq.auth

from keyboard_pub.patch.auth import thread
from keyboard_pub.settings import AUTH_KEYS_PATH, PROTOCOL, HOST, PORT


class Publisher:
    def __init__(self, protocol: str, host: str, port: str):
        public_keys_dir = os.path.join(AUTH_KEYS_PATH, 'public_keys')
        secret_keys_dir = os.path.join(AUTH_KEYS_PATH, 'private_keys')

        context = zmq.Context.instance()

        auth = thread.ThreadAuthenticator(context)
        auth.start()
        auth.configure_curve(domain='*', location=public_keys_dir)

        self.__socket = context.socket(zmq.PUB)

        server_secret_file = os.path.join(secret_keys_dir, 'server.key_secret')
        server_public, server_secret = zmq.auth.load_certificate(server_secret_file)

        self.__socket.curve_secretkey = server_secret
        self.__socket.curve_publickey = server_public
        self.__socket.curve_server = True

        self.__socket.bind('{}://{}:{}'.format(protocol, host, port))

    def send(self, payload: dict):
        self.__socket.send_json(payload)


publisher = Publisher(PROTOCOL, HOST, PORT)
