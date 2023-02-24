import paramiko
import select
import sys

# Set the hostname, username, and password for the SSH connection
hostname = 'rumad.uprm.edu'
username = 'estudiante'
password = ''

# Create a new SSH client object
client = paramiko.SSHClient()

# Automatically add the server's host key to the local HostKeys object
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
client.connect(hostname=hostname, username=username, password=password)

# Open a channel for the SSH session
channel = client.invoke_shell()

# Set the terminal window size for the remote server
channel.resize_pty(width=200, height=50)

# Print the welcome message from the server
print(channel.recv(1024).decode())

# Enter a loop to read input from the user and output from the server
while True:
    # Check if there is any input waiting from the user
    if select.select([sys.stdin], [], [], 0)[0]:
        # Read the input from the user and send it to the server
        user_input = input()
        channel.send(user_input)

    # Check if there is any output waiting from the server
    if select.select([channel], [], [], 0)[0]:
        # Read the output from the server and print it to the console
        output = channel.recv(1024).decode()
        print(output)

# Close the SSH connection
client.close()
