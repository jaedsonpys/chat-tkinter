from tkinter import *
from tkinter import messagebox


def register():
    global name_entry
    username = name_entry.get()

    if len(username) < 1:
        messagebox.showwarning('Aviso', 'Insira um nome de usuário.')
        return

    print(username)


def send_message():
    global message_entry
    message = message_entry.get()

    if len(message) < 1:
        return

    message_entry.delete(0, END)

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

Button(send_message_frame, text='Enviar').pack()

root.mainloop()
