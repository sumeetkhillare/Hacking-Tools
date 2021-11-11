print("Use sudo if you got any error!!!--trypkg")
print("choose from below options...\n1)Mac changer\n2)Arp spoofer")
opt_in=int(input())

def mac_change():
    print("hii")
def arp_spoof():
    print("arp spoof")

def choice(opt):
    switcher = {
            1: lambda: mac_change(),
            2: lambda: arp_spoof()
            # 3: lambda: 'two'
        }
    func = switcher.get(opt, lambda: 'Invalid')
    func()


choice(opt_in)
