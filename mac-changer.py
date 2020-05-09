#!/usr/bin/env python
import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface ,use --help for info")
    elif not options.new_mac:
        parser.error("[-] Please specify new mac address ,use --help for info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " and " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
