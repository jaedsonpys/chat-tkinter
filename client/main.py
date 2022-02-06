from tkinter import *
from tkinter import messagebox

from client_conn import Client
from threading import Thread

client_api = Client()
is_registred = False


def register():
    global name_entry
    username = name_entry.get()

    if len(username) < 1:
        messagebox.showwarning('Aviso', 'Insira um nome de usuário.')
        return

    print(username)
    client_api.register_user(username)


def send_message():
    if not is_registred:
        messagebox.showerror('Erro', 'É necessário informar um nome.')
        return

    global message_entry
    message = message_entry.get()

    if len(message) < 1:
        return

    client_api.send_message(message)
    message_entry.delete(0, END)


def render_message():
    while True:
        global message_list
    
        sender, message = client_api.receive_broadcast()
        full = f'{sender}: {message}'

        message_list.insert(END, full)


root = Tk()

root.geometry('400x400')
root.title('Chat Tkinter - @jaedsonpys')
root.resizable(width=0, height=0)

root.grid_columnconfigure(0, weight=1)

# set_name_frame
set_name_frame = Frame(root)

Label(set_name_frame, text='Seu nome').grid(row=1, column=1)

name_entry = Entry(set_name_frame)
name_entry.grid(row=1, column=2)

Button(set_name_frame, text='Salvar', command=register).grid(row=1, column=3)

set_name_frame.grid_columnconfigure(1, weight=1)
set_name_frame.grid(row=0, column=0)

# message_frame
message_frame = Frame(root)

message_list = Listbox(
    message_frame,
    background='white',
    height=17
)

message_frame.grid(row=2, sticky='nesw')
message_list.pack(fill=BOTH, expand=True, pady=10, padx=10)

# send_message_frame
send_message_frame = Frame(message_frame, height=30)
send_message_frame.pack(fill=X, expand=True, pady=1, padx=10)

message_entry = Entry(send_message_frame, background='white', width=40)
message_entry.pack(side=LEFT)

Button(send_message_frame, text='Enviar', command=send_message).pack()

if not client_api.ping():
    messagebox.showerror('Erro', 'Servidor indisponível')

render_thread = Thread(target=render_message)
render_thread.setDaemon(True)
render_thread.start()

root.mainloop()
