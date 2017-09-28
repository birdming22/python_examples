"""udp echo server"""
from asyncore import dispatcher
from asyncore import loop
import socket


class EchoServer(dispatcher):
    """EchoServer class"""

    def __init__(self, host, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.set_reuse_addr()
        self.bind((host, port))

    # make pylint happy
    @classmethod
    def api_handler(cls, data, addr):
        """handle api"""
        print '%s data:' % repr(addr), data
        return data

    def handle_read(self):
        data, addr = self.recvfrom(8129)
        print 'Incoming connection from %s' % repr(addr)
        rsp = self.api_handler(data, addr)
        if rsp is not None:
            self.sendto(rsp, addr)


if __name__ == '__main__':
    # Host "" means to bind all interface
    # Port 0 means to select an arbitrary unused port
    EchoServer('', 1234)
    loop()
