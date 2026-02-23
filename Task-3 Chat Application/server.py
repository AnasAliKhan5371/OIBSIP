import socket
from tkinter import *

def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Server: "+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))  # encode type

def receive(listbox):
    msg_from_client = client.recv(50)
    listbox.insert('end',"Client: "+msg_from_client.decode('utf-8'))


root=Tk()

entry=Entry(root,width=40,borderwidth=5)
entry.pack(side=BOTTOM)

listbox=Listbox(root,width=40,borderwidth=5)
listbox.pack()

button=Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side = BOTTOM)

rbutton=Button(root,text="Receive",command=lambda :receive(listbox))
rbutton.pack(side = BOTTOM)

root.title('Server')


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AddressFamily_IP address type IPv4,TCP Socket

HOST=socket.gethostname()
PORT=12346

s.bind((HOST,PORT)) # tuple
s.listen(4)
client, address = s.accept()

root.mainloop()