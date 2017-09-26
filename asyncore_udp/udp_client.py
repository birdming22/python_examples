import asyncore
import socket


class EchoClient(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connect((host, port))
        self.send("0000")

    def api_handler(self, data, addr):
        print 'data:', data
        return None

    def handle_read(self):
        data, addr = self.recvfrom(8129)
        print 'Incoming connection from %s' % repr(addr)
        rsp = self.api_handler(data, addr)
        if rsp is not None:
            self.sendto(rsp, addr)

if __name__ == '__main__':
    client = EchoClient('127.0.0.1', 1234)
    asyncore.loop()
