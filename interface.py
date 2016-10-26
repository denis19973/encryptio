from tkinter import *
from encryptio import encrypt_text, decrypt_text, b64encode, b64decode

# ___________INTERFACE

tk = Tk()
tk.title('ImBeCiLe Encryptor')
tk.geometry('550x500')


def print_encrypt(event):
    log.delete(0.0, END)
    log.insert(INSERT, encrypt_text(inp_text.get(), inp_key.get()).decode('utf-8'))

def print_decrypt(event):
    try:
        log_decrypt.delete(0.0, END)
        log_decrypt.insert(INSERT, decrypt_text(inp_text_decrypt.get().encode('utf-8'), inp_key_decrypt.get()))
    except UnicodeDecodeError:
        log_decrypt.insert(INSERT, 'incorrect key.')

def encrypt_mode():
    frame_decrypt.pack_forget()
    frame_encrypt.pack()

def decrypt_mode():
    frame_encrypt.pack_forget()
    frame_decrypt.pack()


# ########ENCRYPT FRAME
frame_encrypt = Frame(tk)

inp_text_label = Label(frame_encrypt, text='input text: ', font='sans-serif')
inp_text_label.pack()


inp_text = Entry(frame_encrypt, font='sans-serif')
inp_text.pack()


inp_text_label = Label(frame_encrypt, text='key(16 bytes): ', font='sans-serif')
inp_text_label.pack()

original_key = StringVar()
inp_key = Entry(frame_encrypt, font='sans-serif', textvariable=original_key)
inp_key.pack()


but_encrypt = Button(frame_encrypt, text='ENCRYPT it', font='sans-serif')
but_encrypt.bind('<Button-1>', print_encrypt)
but_encrypt.pack()

raz = StringVar()
log = Text(frame_encrypt, font='sans-serif', height=15, width=30)
log.pack()
frame_encrypt.pack()

# #####DECRYPT FRAME
frame_decrypt = Frame(tk)

inp_text_label = Label(frame_decrypt, text='input encrypted text: ', font='sans-serif')
inp_text_label.pack()


inp_text_decrypt = Entry(frame_decrypt, font='sans-serif')
inp_text_decrypt.pack()


inp_text_label = Label(frame_decrypt, text='key(16 bytes): ', font='sans-serif')
inp_text_label.pack()

original_key_decrypt = StringVar()
inp_key_decrypt = Entry(frame_decrypt, font='sans-serif', textvariable=original_key)
inp_key_decrypt.pack()


but_encrypt = Button(frame_decrypt, text='DECRYPT it', font='sans-serif')
but_encrypt.bind('<Button-1>', print_decrypt)
but_encrypt.pack()


log_decrypt = Text(frame_decrypt, font='sans-serif', height=15, width=30)
log_decrypt.pack()


main_menu = Menu(tk)
tk.config(menu=main_menu)

fm = Menu(tk)
main_menu.add_cascade(label='Mode', menu=fm)
fm.add_command(label='Encrypt Mode', command=encrypt_mode)
fm.add_command(label='Decrypt Mode', command=decrypt_mode)

tk.mainloop()
