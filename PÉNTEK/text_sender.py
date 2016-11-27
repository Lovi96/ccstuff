import socket


def send_to_server(my_message):
    host = "192.168.150.86"
    port = 12348                   # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(bytes(my_message, encoding="utf-8"))
    data = s.recv(1024)
    s.close()
    print('Received: ' + data.decode("utf-8"))

my_message = input("agyal szoveget:  ")
send_to_server(my_message)
