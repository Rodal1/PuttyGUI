import subprocess

ssh_command = f"ssh -oHostKeyAlgorithms=+ssh-rsa rumad.uprm.edu -l estudiante"

result = subprocess.Popen(ssh_command, shell=True, text=True)

print(result.stdout)
#
#results = dir(result)
#
#print([result.j for j in [i for i in results]])