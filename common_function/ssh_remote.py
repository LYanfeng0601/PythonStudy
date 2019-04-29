#coding=utf-8
import time
import paramiko

def sftp_exec_command(command):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, 22, user, password)
        std_in, std_out, std_err = ssh_client.exec_command(command)
        ssh_client.close()





if __name__ == "__main__":
	host = "192.168.0.103"
	port = 22
	timeout = 30
	user = "root"
	password = "root"
	sftp_exec_command("ls")

