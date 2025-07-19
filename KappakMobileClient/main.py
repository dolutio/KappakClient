#Stable for android kivymd==1.0.2 kivy==2.1.0

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.clock import Clock

from signup_screen import SignUpScreen
from login_screen import LogInScreen
from chats_feed_screen import ChatsFeedScreen
from chat_screen import ChatScreen
from message_tools import Message
from kappak_config import ACCEPT, ACCOUNT_ALREADY_EXIST, ACCOUNT_NOT_FOUND, INCORRECT_PASSWORD, CHAT_ALREADY_EXISTS, CLOSE_CODE
from sendtools import add_message_in_chats_data

import Global

from threading import Thread
import json

class Kappak(MDApp):
    screen_manager: MDScreenManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen_manager = MDScreenManager()

        self.signup_screen = SignUpScreen()
        self.login_screen = LogInScreen()
        self.chats_feed_screen = ChatsFeedScreen()

        Window.bind(on_key_down=self.on_key_down)
        Thread(target=self.make_connection, daemon=True).start()
        Thread(target=self.handle_reply, daemon=True).start()

    def build(self):
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.signup_screen)
        self.screen_manager.add_widget(self.chats_feed_screen)
        self.screen_manager.current = "SignUpScreen"#"ChatsFeed""LogInScreen"

        return self.screen_manager

    def on_key_down(self, win, key, scancode, codepoint, modifiers):
        if key == 27:
            if self.screen_manager.current not in ["SignUpScreen", "LogInScreen"]:
                self.screen_manager.current = "ChatsFeed"
            
            return True
        
        return False
    
    def on_pause(self):
        Global.save_user_data()
        Global.save_chats_data()

        return True
    
    def on_stop(self):
        super().on_stop()

        Global.save_user_data()
        Global.save_chats_data()

    def make_connection(self):
        while True:
            if not Global.user.client_is_connected:
                Global.user.try_to_connect()

                if Global.user.client_is_connected:
                    self.send_update_messages_req()
    
        
    def handle_reply(self):
        while True:
            reply = Global.user.decode_reply()

            if type(reply) is int:
                Clock.schedule_once(lambda dt: self.handle_num_codes(reply)) # handle_num_codes works with kivy widgets

            if type(reply) is str:
                self.update_msgs(reply)

    def handle_num_codes(self, reply: int):
        if self.screen_manager.current == 'SignUpScreen':
            if reply == ACCOUNT_ALREADY_EXIST:
                self.screen_manager.get_screen('SignUpScreen').account_is_already_notify()

            if reply == ACCEPT:
                self.screen_manager.get_screen('SignUpScreen').save_account_data()
                self.screen_manager.current = 'ChatsFeed'
                print("Accepted")

        if self.screen_manager.current == 'LogInScreen':
            if reply == ACCOUNT_NOT_FOUND:
                self.screen_manager.get_screen('LogInScreen').account_not_found_notify()

            if reply == INCORRECT_PASSWORD:
                self.screen_manager.get_screen('LogInScreen').incorrect_password_notify()

            if reply == ACCEPT:
                self.screen_manager.get_screen('LogInScreen').save_account_data()
                self.screen_manager.current = 'ChatsFeed'
        
        if reply == CLOSE_CODE:
            Global.user.close_client()

    def send_update_messages_req(self):
        req_dict = dict()

        for chat_name, chat in Global.chats_data.items():
            print(chat)
            req_dict.update({chat_name: chat['last_received_msg_id']})

        if Global.user.authed:
            print("lll")
            Global.user.send_req(f'update {json.dumps(req_dict)}')         
    
    def update_msgs(self, chats_json_s: str):
        msg_id = add_message_in_chats_data(chats_json_s)
        msg_data = Global.chats_data[Global.current_chat_name][msg_id]
        msg_text = msg_data['text']
        msg_sending_time = msg_data['sending_time']

        message = Message(text=msg_text, sending_time=msg_sending_time, message_id=msg_id)
        Clock.schedule_once(lambda dt: self.screen_manager.get_screen(Global.current_chat_name).message_show_place.add_message(message))        

def main():
    app = Kappak()

    app.run()

def connect_to_server():
    pass

def filter_censorship():
    if Global.user.need_to_filter_censoreship:
        pass

if __name__ == '__main__':
    main()
