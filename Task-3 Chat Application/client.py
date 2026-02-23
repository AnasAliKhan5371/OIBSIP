import socket
from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',"Client: "+ message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))

    receive(listbox)

def receive(listbox):
    message=s.recv(50)
    listbox.insert('end', "Server: " + message.decode('utf-8'))

root=Tk()

entry=Entry(root,width=40,borderwidth=5)
entry.pack(side=BOTTOM)

listbox=Listbox(root,width=40,borderwidth=5)
listbox.pack()

button=Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side = BOTTOM)

rbutton=Button(root,text="Receive",command=lambda :receive(listbox))
rbutton.pack(side = BOTTOM)
root.title('Client')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AddressFamily_IP address type IPv4,TCP Socket

HOST=socket.gethostname()
PORT=12346

s.connect((HOST,PORT))

root.mainloop()