#Stable for android kivymd==1.0.2 kivy==2.1.0

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

from signup_screen import SignUpScreen
from login_screen import LogInScreen
from chats_feed_screen import ChatsFeedScreen
from chat_screen import ChatScreen
from message_tools import Message
from kappak_config import ACCEPT, ACCOUNT_ALREADY_EXIST, ACCOUTN_NOT_FOUND, INCORRECT_PASSWORD

import Global

from threading import Thread

class Kappak(MDApp):
    screen_manager: MDScreenManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen_manager = MDScreenManager()

        self.signup_screen = SignUpScreen()
        self.login_screen = LogInScreen()
        self.chats_feed_screen = ChatsFeedScreen()

        Window.bind(on_keyboard=self.on_key_down)

    def build(self):
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.signup_screen)
        self.screen_manager.add_widget(self.chats_feed_screen)
        self.screen_manager.current = "SignUpScreen"#"ChatsFeed""LogInScreen"

        return self.screen_manager

    def on_key_down(self, win, key, *b):
        if key == 27:
            # if self.screen_manager.current not in ["SignUpScreen", "LogInScreen"]:
                # self.screen_manager.current = "ChatsFeed"
            
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

    def socket_process(self):
        if not Global.user.client:
            Global.user.try_to_connect()

            return

    def handle_num_codes(self):
        reply = Global.user.decode_reply()

        if self.screen_manager.current == 'SignUpScreen':
            if reply == ACCOUNT_ALREADY_EXIST:
                self.screen_manager.get_screen('SignUpScreen').account_is_already_notify()

        if self.screen_manager.current == 'LogInScreen':
            if reply == ACCOUTN_NOT_FOUND:
                self.screen_manager.get_screen('LogInScreen').account_not_found_notify()

            if reply == INCORRECT_PASSWORD:
                self.screen_manager.get_screen('LogInScreen').incorrect_password_notify
                
    
    def update_msgs(self):
        ...
        chats_json = {"MAIN_CHAT":{"last_received_msg_id": "supermarchok1", "supermarchok1": {"text": "Hellow!", "sending_time": "01:07:2025:15:11"}}}

        for chat_name, chat in chats_json.items():
            Global.chats_data[chat_name].update(chat)

            chat_screen: ChatScreen = self.screen_manager.get_screen(chat_name)
            for msg_id, msg in chat.items():
                if msg_id != "last_received_msg_id":
                    chat_screen.message_show_place.add_message(Message(message_id=msg_id, sending_time=msg["sending_time"], text=msg["text"]))

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