from tkinter import *
from tkinter import messagebox


def register():
    global name_entry
    username = name_entry.get()

    print(username)

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

root.mainloop()
