#!/usr/bin/env python
import optparse
import subprocess
import re


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


def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])
    mac_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)

    if mac_res:
        return mac_res.group(0)
    else:
        print("Could not read mac")



def main():
    print("Use sudo if you got any error!!!")
    options = get_arguments()
    cur_mac = get_current_mac(options.interface)
    print("Current MAC: " + str(cur_mac))
    change_mac(options.interface, options.new_mac)
    cur_mac = get_current_mac(options.interface)

    if cur_mac==options.new_mac:
        print("Changed Successfully")
    else:
        print("error")


if __name__ == "__main__":
    main()
