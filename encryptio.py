from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64encode, b64decode


print('AES block size: {0}'.format(AES.block_size))
# CFB_IV
cfb_iv = Random.new().read(AES.block_size)


# ___________________TEXT

def encrypt_text(plain_text, original_key):
    key = original_key.encode('utf-8')[0:32]
    plain_text = plain_text.encode('utf-8')
    cfb_cipher_encrypt = AES.new(key, AES.MODE_CFB, cfb_iv)
    cfb_msg_encrypt = b64encode(cfb_cipher_encrypt.encrypt(plain_text))
    print('Encrypt text {} :'.format(cfb_msg_encrypt.decode('utf-8')))
    return cfb_msg_encrypt


def decrypt_text(encrypt_text, original_key):
    key = original_key.encode('utf-8')[0:32]
    cfb_cipher_decrypt = AES.new(key, AES.MODE_CFB, cfb_iv)
    cfb_msg_decrypt = cfb_cipher_decrypt.decrypt(b64decode(encrypt_text)).decode('utf-8')
    print('Decrypt text {}'.format(cfb_msg_decrypt))
    return cfb_msg_decrypt


# a = encrypt_text('22222342', '90qwerty12345678')
# decrypt_text(a, '90qwerty12345678')


# ___________________FILES
def encrypt_file(file, original_key):
    key = original_key.encode('utf-8')[0:32]
    with open(file, 'rb') as f:
        bites_data = f.read()

    print('File: {}'.format(bites_data.decode('utf-8')))
    cfb_cipher_encrypt = AES.new(key, AES.MODE_CFB, cfb_iv)
    cfb_msg_encrypt = b64encode(cfb_cipher_encrypt.encrypt(bites_data))

    with open(file, 'wb') as f:
        f.write(cfb_msg_encrypt)

    print('Encrypted file: {}'.format(cfb_msg_encrypt.decode('utf-8')))


def decrypt_file(file, original_key):
    print('Your key is: {}'.format(original_key))
    key = original_key.encode('utf-8')[0:32]
    with open(file, 'rb') as f:
        encrypted_data = f.read()

    cfb_cipher_decrypt = AES.new(key, AES.MODE_CFB, cfb_iv)
    cfb_msg_decrypt = cfb_cipher_decrypt.decrypt(b64decode(encrypted_data))

    with open(file, 'wb') as f:
        f.write(cfb_msg_decrypt)

    print('OK.')

    print('File decrypt: {0}'.format(cfb_msg_decrypt.decode('utf-8')))


#####################################################

encrypt_file('raz.txt', '90qwerty12345678')
decrypt_file('raz.txt', '90qwerty12345678')

# ___________INTERFACE
from tkinter import *
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
