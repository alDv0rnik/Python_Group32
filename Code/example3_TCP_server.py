import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 8888))
    sock.listen()

    while True:
        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            break
        else:
            res = client.recv(1024)
            print(f'Message {res.decode("utf-8")}')
