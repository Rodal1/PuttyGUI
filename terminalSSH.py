#import paramiko
#
#command = ""
#
#host = "rumad.uprm.edu"
#username = ""
#password = ""
#
#client = paramiko.client.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect(host, username=username, password=password)
#
#_stdin, _stdout,_stderr = client.exec_command("estudiante")
#
#print(_stdout.read().decode())
#client.close()

import subprocess

ssh_command = f"ssh rumad.uprm.edu -l estudiante"

result = subprocess.run(ssh_command,shell=True, capture_output=True, text=True)

print(result.stderr)