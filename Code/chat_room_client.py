import socket

USERNAME = "Roman"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.10.60', 8888))

is_accept =True

while is_accept:
    prompt = input(f"[{USERNAME}]: ")
    client.send(f"[{USERNAME}]: {prompt}".encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'end':
        is_accept = False
    else:
        print(msg)
