try:
    import nmap
except:
    import os
    exit_code = os.system('pip3 install python-nmap')
    if (exit_code is not 0):
        print('Error running pip3 most probably due to, pip3 command not found')
    else:
        print('Successfully installed python-nmap')
        import nmap

ps = nmap.PortScanner()

def portScanner(host=None, hostPort=None):
    if (host is None):
        host= input("host : ") or 'localhost'
    if (hostPort is None):
        hostPort = input('port [port range] : ') or '20-3000'

    response = ps.scan(host, hostPort)
    print(response)

    for host in ps.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, ps[host].hostname()))
        print('State : %s' % ps[host].state())
        for iproto in ps[host].all_protocols():
            print('----------')
            print('Protocol : %s' % iproto)
            lport = ps[host][iproto].keys()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, ps[host][iproto][port]['state']))


