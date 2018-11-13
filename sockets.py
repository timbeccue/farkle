
import socket

# Create TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = host = 'localhost' #socket.gethostname()

# Get fully qualified hostname.
local_fqdn = socket.getfqdn()

ip_address = socket.gethostbyname(local_hostname)

print(f"working on {local_hostname}({local_fqdn}) with {ip_address}.")

server_address = (ip_address, 23456)
print ("startign up on %s port %s" % server_address)
sock.bind(server_address)

sock.listen(1)

while True:

    print ("waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print ('connection from', client_address)

        while True:
            data = connection.recv(64)
            if data:
                print(f'Data: {data}')
            else:
                print ("no more data.")
                break
    finally:
        connection.close()
