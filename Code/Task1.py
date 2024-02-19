"""
Открыть клиентский TCP сокет на smtp.gmail.com (порт 587),
сказать в сокет "GET", получить ответ, сохранить в файл

1) откройте клиентский TCP сокет на smtp.gmail.com порт 587
2) поздоровайтесь с гуглом, скажите "EHLO google.com" (здесь не опечатка, именно EHLO)
3) ответ получите и выведите на экран
"""
import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("smtp.gmail.com", 587))

    msg = sock.recv(1024).decode('utf-8')
    print(f"s -> c: {msg}")

    msg1 = "EHLO google.com \r\n"
    sock.send(msg1.encode('utf-8'))
    print(f"c -> s: {msg1}")

    msg = sock.recv(1024).decode('utf-8')
    print(f"s -> c: {msg}")