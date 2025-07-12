import socket
import threading
import struct

from kappak_crypt import kappak_hash

HOST = '192.168.1.8'
PORT = 8080

class User:
    username: str = ''
    pwd_hash: str = ''
    __age: int = 0
    adulthood_in_USA: int = 21
    the_last_sended_message_id: int = 0
    need_to_filter_censoreship: bool = True
    signed_up: bool = False
    client: socket.socket
    client_is_connected: bool = False
    not_sended_requests: list = list()

    def __init__(self, name: str = '', pwd_hash: str = '', age: int = 0, the_last_sended_message_id: int = 0, need_to_filter_censoreship=True):
        self.username = name
        self.pwd_hash = pwd_hash
        self.__age = age
        self.the_last_sended_message_id = the_last_sended_message_id

        if self.__age <= self.adulthood_in_USA and not need_to_filter_censoreship:
            self.need_to_filter_censoreship = True

        if self.username != '':
            self.signed_up = True


        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(5)
    
    def get_user_data(self):
        user_data = {
            'username': self.username,
            'pwd_hash': self.pwd_hash,
            'age': self.__age,
            'the_last_sended_message_id': self.the_last_sended_message_id,
            'need_to_filter_censoreship': self.need_to_filter_censoreship
        }

        return user_data
    
    def try_to_connect(self):
        try:
            if self.client.fileno() == -1: # Socket closed
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.client.connect((HOST, PORT))
            self.client_is_connected = True

            if self.username and self.pwd_hash:
                self.login()
        
        except OSError:
            self.client_is_connected = False # Server do not found
    
    def send_req(self, request: str):
        print("req:", self.client_is_connected)
        if self.client and self.client_is_connected:
            try:
                for not_sended_request in self.not_sended_requests:
                    self.client.sendall(not_sended_request.encode())

                self.client.sendall(request.encode())
            except BrokenPipeError:
                print("Server closed")
                self.client_is_connected = False
        
        else:
            self.not_sended_requests.append(request)

    def recv_all(self, expected_len):
        data = b''

        while (len(data) < expected_len):

            try:
                part = self.client.recv(expected_len - len(data))

                print("Socket Timeout")

                if not part: # if part == b'' server closed connection
                    print("Вы не в сети")
                    self.client_is_connected = False
            
                    return None

                data += part

                return data
            
            except socket.timeout: # Server just not send the datas
                ...


    def recv_reply(self):
        if self.client:
            reply_type_recv = self.recv_all(1)
            if reply_type_recv:
                reply_type = reply_type_recv[0]
                reply_len = int.from_bytes(self.recv_all(2), 'big')
                reply = self.recv_all(reply_len)

                return reply_type, reply
        
        return None, None
    
    def decode_reply(self):
        reply_type, reply = self.recv_reply()

        if reply_type is None:
            return 0

        if reply_type == 0x01: # String
            return reply.decode()
        
        elif reply_type == 0x02: # NumCode
            return int.from_bytes(reply, 'big')
        
        return 0 # Undefined reply
    
    def login(self, username: str = '', password: str = ''):
        if username and password:
            self.send_req(f'login {username} {kappak_hash(password)}')

            return
        
        self.send_req(f'login {self.username} {self.pwd_hash}')
    
    def close_client(self):
        self.client.close()
        self.client_is_connected = False

    def serializate(self):
        username_length = len(self.username)

        data = (self.username, username_length, self.__age, self.need_to_filter_censoreship)

        return struct.pack(f'{username_length}siib', *data)

    def deserializate(self):
        data = ()

        return struct.unpack()

# user = User('martun', 16, 0, True)
# user.send_req(f's martun {1}')
# print("Reply:", user.recv_reply())
