"""pcap parse example
Problem: Scapy_Exception("Not a pcap capture file (bad magic)")
Solution: In wireshark 'Save as': Wireshark/tcpdump -pcap
"""

from scapy.all import rdpcap
from scapy.all import IP
from scapy.all import UDP
from scapy.all import Raw


def pcap_parse():
    """parse pcap file"""
    packets = rdpcap('sample.pcap')

    for packet in packets:
        packet.show()
        print 'ip len', packet[IP].len
        print 'ip len', packet[IP].src
        print 'ip len', packet[IP].dst
        print 'udp len', packet[UDP].len
        print 'Raw len', len(packet[Raw])
        print 'modify dst ip to 10.10.101.254'
        packet[IP].dst = "10.10.101.254"
        packet.show()


if __name__ == '__main__':
    pcap_parse()
