import tkinter as tk
from socket import *
from _thread import *
import threading

socket_file_discriptor = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000

wind = tk.Tk()
wind.geometry('300x400')
tk.Label(wind, text='Enter message: ').grid(row=0)
e1 = tk.Entry(wind, width=30)
e1.grid(row=0, column=1)
l=tk.Label(wind, text = 'recieved messages').grid(row = 1, column = 0)
rm = tk.Entry(wind, width=30)
rm.grid(row = 1, column=1)


def recieved_thread(c):
    while True:
        x = c.recv(2048)
        rm.delete(0, len(rm.get()))
        #l.config(text = x)
        rm.insert(0, x)
        

socket_file_discriptor.connect((host, port))
start_new_thread(recieved_thread, (socket_file_discriptor,))


def send():
    socket_file_discriptor.send(e1.get().encode("utf=8"))
    e1.delete(0, len(e1.get()))


btn = tk.Button(wind, text="send", width=10, command=send)
btn.grid(row=3, column=1)
tk.mainloop()
