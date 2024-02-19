import socket


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('127.0.0.1', 8888))

    while True:
        try:
            res = sock.recv(1024)
        except KeyboardInterrupt:
            sock.close()
            break
        else:
            print(f'Message {res.decode("utf-8")}')
