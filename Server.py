from socket import *
from _thread import *
import threading

socket_file_discriptor = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
socket_file_discriptor.bind((host, port))
socket_file_discriptor.listen(5)
clients = [] #list of all clients (thier session numbers)

def connect_new_user(session_number, client_info):
    print(client_info[0] + " connected.")
    while True:
        message = session_number.recv(2048)
        message = client_info[0] + ':' + message.decode('utf=8')
        send_to_all(message, session_number)

##################################################
def send_to_all(message, session_number):
    for client in clients:
        if client != session_number:
            client.send(message.encode("utf=8"))
#################################################
while True:
    session, client_info = socket_file_discriptor.accept()
    clients.append(session)
    start_new_thread(connect_new_user, (session, client_info))
session.close()

