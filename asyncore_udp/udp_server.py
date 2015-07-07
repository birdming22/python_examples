import asyncore
import socket


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.set_reuse_addr()
        self.bind((host, port))

    def api_handler(self, data, addr):
        print 'data:', data
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
    server = EchoServer('', 1234)
    asyncore.loop()
