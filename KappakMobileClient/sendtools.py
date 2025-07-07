import Global

from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.textinput import TextInput

from message_tools import MessagesShowPlace, Message

import time
import json

def get_message_name() -> str:
    i += 1

    return ''

def send_message():
    if Global.message_input_box.text: #if text == '', not send the message
        msg_text = Global.message_input_box.text
        sending_time = time.strftime("%d:%m:%Y:%H:%M")
        msg_id = Global.user.username + str(Global.user.the_last_sended_message_id)

        Global.messages_show_place_widget.add_message(Message(text=msg_text, sending_time=sending_time, message_id=msg_id))
        i = 0

        msg_json = {Global.current_chat_name: {msg_id: {"text": msg_text, "sending_time": sending_time}}}

        Global.user.send_req("m " + json.dumps(msg_json))
        Global.chats_data[Global.current_chat_name].update(msg_json[Global.current_chat_name])

        Global.message_input_box.text = ''
    
    else:print(Global.message_input_box)

class MessageInputBox(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (0.9, 1)
        self.multiline = True
        self.cursor_color = (0, 1, 0, 1)
        self.background_color = (1, 1, 1, 1)
        self.font_name = 'DejaVuSans.ttf'

    def on_text_validate(self):
        send_message()

class SendButton(MDFillRoundFlatButton):
    text = 'Send'
    md_bg_color = (0.0, 0.35, 0.62, 1)# old version - (1, 0, 0, 1)
    line_color = (0, 0, 0, 0)
    halign = 'center'
    text_color = (1, 1, 1, 1)
    font_name = 'DejaVuSans.ttf'
    font_size = 30

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (0.05, 1)
        self.pos_hint = {'x': 0.85, 'y': 0}

    def on_release(self):
        send_message()