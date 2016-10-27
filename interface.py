from tkinter import *
from cipher_core import encrypt_text, decrypt_text

# ___________INTERFACE

tk = Tk()
tk.title('ImBeCiLe Encryptor')
tk.geometry('550x500')


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # FONT for labels and fields
        self.font = 'sans-serif'
        self.pack()
        self.show_menu()
        self.create_encrypt_frame()

    def create_encrypt_frame(self) -> object:
        self.frame_encrypt = Frame(tk)

        self.inp_text_label = Label(self.frame_encrypt, text='input text: ', font=self.font)
        self.inp_text_label.pack()
        self.inp_text = Entry(self.frame_encrypt, font=self.font)
        self.inp_text.pack()

        self.inp_text_label = Label(self.frame_encrypt, text='key(16 bytes): ', font=self.font)
        self.inp_text_label.pack()

        self.original_key = StringVar()
        self.inp_key = Entry(self.frame_encrypt, font=self.font, textvariable=self.original_key)
        self.inp_key.pack()

        self.but_encrypt = Button(self.frame_encrypt, text='ENCRYPT it', font=self.font)
        self.but_encrypt.bind('<Button-1>', self.print_encrypt)
        self.but_encrypt.pack()

        self.raz = StringVar()
        self.log = Text(self.frame_encrypt, font=self.font, height=15, width=30)
        self.log.pack()

        self.frame_encrypt.pack()

    def create_decrypt_frame(self):
        self.frame_decrypt = Frame(tk)

        self.inp_text_label = Label(self.frame_decrypt, text='input encrypted text: ', font=self.font)
        self.inp_text_label.pack()

        self.inp_text_decrypt = Entry(self.frame_decrypt, font=self.font)
        self.inp_text_decrypt.pack()

        self.inp_text_label = Label(self.frame_decrypt, text='key(16 bytes): ', font=self.font)
        self.inp_text_label.pack()

        self.original_key_decrypt = StringVar()
        self.inp_key_decrypt = Entry(self.frame_decrypt, font=self.font, textvariable=self.original_key_decrypt)
        self.inp_key_decrypt.pack()

        self.but_encrypt = Button(self.frame_decrypt, text='DECRYPT it', font=self.font)
        self.but_encrypt.bind('<Button-1>', self.print_decrypt)
        self.but_encrypt.pack()

        self.log_decrypt = Text(self.frame_decrypt, font=self.font, height=15, width=30)
        self.log_decrypt.pack()
        self.frame_decrypt.pack()

    def use_encrypt(self):
        self.frame_decrypt.pack_forget()
        self.create_encrypt_frame()

    def use_decrypt(self):
        self.frame_encrypt.pack_forget()
        self.create_decrypt_frame()

    def print_encrypt(self, event):
        self.log.delete(0.0, END)
        self.log.insert(INSERT, encrypt_text(self.inp_text.get(), self.inp_key.get()).decode('utf-8'))

    def print_decrypt(self, event):
        try:
            self.log_decrypt.delete(0.0, END)
            self.log_decrypt.insert(INSERT, decrypt_text(self.inp_text_decrypt.get().encode('utf-8'),
                                                         self.inp_key_decrypt.get()))
        except UnicodeDecodeError:
            self.log_decrypt.insert(INSERT, 'incorrect key.')

    def show_menu(self):
        main_menu = Menu(tk)
        tk.config(menu=main_menu)

        fm = Menu(tk)
        main_menu.add_cascade(label='Mode', menu=fm)
        fm.add_command(label='Encrypt Mode', command=self.use_encrypt)
        fm.add_command(label='Decrypt Mode', command=self.use_decrypt)


app = Application(master=tk)
