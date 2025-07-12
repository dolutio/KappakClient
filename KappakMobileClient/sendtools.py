import Global

from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp

from message_tools import MessagesShowPlace, Message
from kappak_crypt import kappak_crypt

import time
import json
import copy

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

        Global.chats_data[Global.current_chat_name].update(msg_json[Global.current_chat_name])

        msg_json_req = copy.deepcopy(msg_json) # for dont change the local msg_json
        msg_json_req[Global.current_chat_name][msg_id]['text'] = kappak_crypt(msg_text.encode(), Global.current_chat_name + msg_id, custom_key_word=Global.chats_data[Global.current_chat_name]["custom_key"]).hex()
        
        print(msg_json_req, msg_json)

        Global.user.send_req("message " + json.dumps(msg_json_req))

        Global.user.the_last_sended_message_id += 1
        Global.message_input_box.text = ''
    
    else:print(Global.message_input_box)

def add_message_in_chats_data(msg_json_s):
    print(repr(msg_json_s), type(msg_json_s), "\n"*100)
    msg_json = json.loads(msg_json_s)

    chat_name = next(iter(msg_json))
    msg_id = next(iter(msg_json[chat_name]))

    msg_json[chat_name][msg_id]['text'] = kappak_crypt(bytearray.fromhex(msg_json[chat_name][msg_id]['text']), chat_name + msg_id, custom_key_word=Global.chats_data[Global.current_chat_name]["custom_key"], enc=False).decode() # decrypt

    print('\n'* 10, 'TEst', Global.chats_data,)
    Global.chats_data[chat_name].update(msg_json[chat_name]) # if do without chat_name, the data is rewriting
    print(Global.chats_data, "\n"*10)

    return msg_id

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
    font_size = dp(30)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (None, 1)
        self.size = (dp(50), dp(50))

        Window.bind(size=self.set_pos_hint_for_phones)

        self.set_pos_hint_for_phones(None, None) # for first position

    def set_pos_hint_for_phones(self, instance, size):
        self.pos = (Window.width - dp(100), dp(0))

    def on_release(self):
        send_message()
