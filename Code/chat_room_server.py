import socket

USERNAME = "Alex"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))

sock.listen()
client, addr = sock.accept()

is_accept = True

while is_accept:
    msg = client.recv(1024).decode('utf-8')
    if msg.endswith('end'):
        is_accept = False
    else:
        print(msg)
        prompt = input(f"[{USERNAME}]: ")
        if prompt == 'end':
            break
        client.send(f"[{USERNAME}]: {prompt}".encode('utf-8'))
