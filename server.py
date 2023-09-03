import socket
import threading
import queue

print("server Is Running...")
messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", 9090))

def recieve():
    # Accepting the messages and storing the messages in queue.
    while True:
        try:
            message, addr = server.recvfrom(1024)
            messages.put(messages, addr)
        except Exception as e:
            pass

def broadcast():
    # It will Take all the Messasges and send them to the client
    while True:
        while not messages.empty():
            print(messages)
            message, addr = list(messages.get())
            print(message.decode())
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":")+1:]
                        server.sendto(f"{name} joined!".encode(), client)
                    else:
                        server.sendto(message, client)
                except Exception as e:
                    clients.remove(client)

t1 = threading.Thread(target=recieve)
t2 = threading.Thread(target=broadcast)
t1.start()
t2.start()