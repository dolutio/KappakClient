import socket
import hashlib
import struct

HOST = '192.168.1.11'
PORT = 1234

UNICODE_MAX_VALUE = 0x10FFFF
name = 'MAIN_CHAT'

def gen_custom_key(custom_key_text: str) -> int:
    custom_key: int = 0

    if custom_key_text.isdigit():
        custom_key = int(custom_key_text)

    else: 
        for i, ch in enumerate(custom_key_text):
            custom_key += ord(custom_key_text[i]) + i % 7

    return custom_key

def kappak_hash(word: str):
    for indx, ch in enumerate(word):
        word = word[:indx] + chr((ord(ch) + (indx + 1) * 1000) % UNICODE_MAX_VALUE) + word[indx+1:]
    
    return hashlib.sha256(word.encode())

def kappak_encrypt(bytes_: bytearray, key_word: str, custom_key_word: str = '', enc=True) -> bytearray: # keyword is chat_name
    crypted_bytes = bytearray()

    for i, b in enumerate(bytes_): # index, byte
        step = ord(key_word[i]) + gen_custom_key(custom_key_word)
        if not enc:
            step = -step
        crypted_bytes.append(((b + step) % 257 + 257) % 257)

    return crypted_bytes

# print(gen_custom_key("_orei849_IIkwskixs9"))
print(kappak_encrypt(kappak_encrypt("hello".encode(), name, 'TUMO_CH'), name, 'TUMO_CH', False))
# print(kappak_hash(input(':')))            

class ClientUser:
    username = 'jafar'
    password = str(hashlib.sha256("hhhh".encode()))

    def ser(self):
        return struct.pack(f'{len(self.username)}s32s', self.username.encode(), self.password.encode())
    def send_req(self, request: str):
        client.sendall(request)

text = 'Hello, muthefaka!\n'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# client.sendall(ClientUser().ser())
client.sendall("")

print(struct.unpack('32s', client.recv(32)))

client.close()