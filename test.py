import socket
import ssl


initial_url = "https://127.0.0.1" 
url_parts = initial_url.split("//")[1].split("/", 1)
hostname = url_parts[0]
path = url_parts[1] if len(url_parts) > 1 else "/"



context = ssl.create_default_context()
sock = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
server_address = (hostname, 443)
sock.connect(server_address)
request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
sock.sendall(request.encode())


response = b""
while True:
    data = sock.recv(1024)
    if not data:
        break
    response += data


response_str = response.decode()
if response_str.startswith("HTTP/1.0 301") or response_str.startswith("HTTP/1.1 301"):
    location_header = response_str.split("Location: ")
    if len(location_header) > 1:
        new_url = location_header[1].split("\r\n")[0].strip()
        sock.close()

        new_url_parts = new_url.split("//")[1].split("/", 1)
        new_hostname = new_url_parts[0]
        new_path = new_url_parts[1] if len(new_url_parts) > 1 else "/"

        new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_server_address = (new_hostname, 80)
        new_sock.connect(new_server_address)

        new_request = f"GET {new_path} HTTP/1.1\r\nHost: {new_hostname}\r\nConnection: close\r\n\r\n"
        new_sock.sendall(new_request.encode())

        new_response = b""
        while True:
            data = new_sock.recv(1024)
            if not data:
                break
            new_response += data
        print(new_response.decode())
    else:
        print("Location header not found in the response.")
else:

    print(response_str)

sock.close()