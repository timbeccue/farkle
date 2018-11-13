import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = 'localhost' #socket.gethostname()

local_fqdn = socket.getfqdn()

ip_address = socket.gethostbyname(local_hostname)

server_address = (ip_address, 23456)
sock.connect(server_address)
print(f"connecting to {local_hostname}({local_fqdn}) with {ip_address}.")

# Define data to be sent to the server.
temperature_data = ['15', '22', '21', '32', '34', '221']
for entry in temperature_data:
    print (f'data: {entry}')
    new_data = str(f'temperature: {entry}\n').encode('utf-8')
    sock.sendall(new_data)
    #time.sleep(.2)

sock.close()
