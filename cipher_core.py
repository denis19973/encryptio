from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64encode, b64decode

print('AES block size: {0}'.format(AES.block_size))
# CFB_IV
#TODO remove hardcode
cfb_iv = '1234567890qwerty'

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