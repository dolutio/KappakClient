print("Started....", '\n'*10)

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDFillRoundFlatButton

from threading import Thread
import socket

HOST = '192.168.1.8'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server():
    client.connect((HOST, PORT))

def disconnect_to_server():
    client.close()

class TestClientAPP(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.float_layout = MDFloatLayout()
        self.input_box = MDTextFieldRect()
        self.send_button = MDFillRoundFlatButton(text='Send', on_release=self.send)

        self.float_layout.add_widget(self.input_box)
        self.float_layout.add_widget(self.send_button)

        connect_to_server()

    def build(self):
        return self.float_layout

    def send(self, *args):
        client.sendall(self.input_box.text.encode('utf-8'))
        self.input_box.text = ''

TestClientAPP().run()