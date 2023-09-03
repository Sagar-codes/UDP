import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8000, 9000)))

name  = input("Name: ")

def recieve():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except Exception as e:
            pass

t = threading.Thread(target=recieve)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", 9090))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("localhost", 9090))