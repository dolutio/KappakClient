import hashlib

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

def kappak_crypt(bytes_: bytearray, key_word: str, custom_key_word: str = '', enc=True) -> bytearray: # keyword is chat_name
    crypted_bytes = bytearray()
    key_word_len = len(key_word)

    for i, b in enumerate(bytes_): # index, byte
        step = ord(key_word[i % key_word_len]) + gen_custom_key(custom_key_word)
        if not enc:
            step = -step
        crypted_bytes.append(((b + step) % 257 + 257) % 257)

    return crypted_bytes