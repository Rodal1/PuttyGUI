import paramiko

# Create an SSH client object
client = paramiko.SSHClient()

# Set the policy to automatically add the hostname to the list of known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
client.connect(hostname='rumad.uprm.edu', username='estudiante', password='')

# Open an SSH channel
channel = client.invoke_shell()

# Send a command to the SSH channel
# channel.send('')

# Wait for the command to execute and print the output
while not channel.recv_ready():
    pass

output = channel.recv(1024).decode('utf-8')
print(output)

# Close the SSH channel and client connection
channel.close()
client.close()


