import Global

from kivymd.uix.floatlayout import MDFloatLayout
from sendtools import MessageInputBox, SendButton
from kivy.uix.textinput import TextInput
from kivymd.uix.toolbar import MDTopAppBar

class AdreesseInfo(MDTopAppBar):
    adreesse_name = 'User'
    
    def __init__():
        pass

class SendBar(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_input_box = MessageInputBox()
        self.send_button = SendButton()

        self.build()

    def build(self):
        self.add_widget(self.message_input_box)
        self.add_widget(self.send_button)