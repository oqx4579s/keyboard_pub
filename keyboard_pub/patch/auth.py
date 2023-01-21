import zmq
from zmq.auth import thread
from zmq.auth.base import Authenticator


class AuthenticationThread(thread.AuthenticationThread):
    def __init__(
            self,
            authenticator: Authenticator,
            pipe: zmq.Socket,
    ) -> None:
        super().__init__(authenticator, pipe)
        self.daemon = True


thread.AuthenticationThread = AuthenticationThread
