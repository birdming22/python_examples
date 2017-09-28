"""udp client example"""
from asyncore import dispatcher
from asyncore import loop
import socket


class EchoClient(dispatcher):
    """udp client class"""

    def __init__(self, host, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connect((host, port))
        self.send("0000")

    # make pylint happy
    @classmethod
    def api_handler(cls, data, addr):
        """hande api"""
        print '%s data:' % repr(addr), data
        return None

    def handle_read(self):
        data, addr = self.recvfrom(8129)
        print 'Incoming connection from %s' % repr(addr)
        rsp = self.api_handler(data, addr)
        if rsp is not None:
            self.sendto(rsp, addr)


if __name__ == '__main__':
    EchoClient('127.0.0.1', 1234)
    loop()
