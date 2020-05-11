#!/usr/bin/env python
 # execute this command before running programme:- iptables -I FORWARD -j NFQUEUE --queue-num 0
 #iptables --flush ///to delete

import netfilterqueue


def process_packet(packet):
    print(packet)
    packet.drop()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

