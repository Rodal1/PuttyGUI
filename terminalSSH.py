import paramiko

command = ""

host = "rumad.uprm.edu"
username = ""
password = ""

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

_stdin, _stdout,_stderr = client.exec_command("estudiante")

print(_stdout.read().decode())
client.close()
