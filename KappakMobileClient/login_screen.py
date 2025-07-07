from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextField

from login_tools import AuthUserNameInputBox, AuthPassWordInputBox, AuthButton, GoToAuthScreenButton

from kappak_user import User
from kappak_crypt import kappak_hash

import json
import Global

class LogInScreen(MDScreen):
    name = "LogInScreen"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.md_bg_color = (0.05, 0.08, 0.12, 1)

        self.box = MDFloatLayout()

        self.login_username_input_box = AuthUserNameInputBox()
        self.login_password_input_box = AuthPassWordInputBox()

        self.btn = AuthButton(text='LogIn', on_released=self.login)

        self.go_to_signup_screen_button = GoToAuthScreenButton(text='Have not an account? Sign Up', on_release=self.go_to_signup_screen)

        self.build()

    def build(self):
        self.box.add_widget(self.login_username_input_box)
        self.box.add_widget(self.login_password_input_box)
        self.box.add_widget(self.btn)
        self.box.add_widget(self.go_to_signup_screen_button)

        self.add_widget(self.box)
    
    def on_parent(self, widget, parent):
        self.setup_user() #When the widget have a parent
    
    def get_user_data(self):
        try:
            with open("user_data.json", 'r') as user_data_file:
                user_data = json.load(user_data_file)
        
        except FileNotFoundError:
            user_data = None
        
        return user_data
    
    def setup_user(self):
        user_data = self.get_user_data()

        if user_data is not None:
            name = user_data['username']
            age = user_data['age']
            need_to_filter_censoreship = user_data['need_to_filter_censoreship']
            the_last_sended_message_id  = user_data['the_last_sended_message_id']
    
            Global.user = User(name, age, the_last_sended_message_id, need_to_filter_censoreship)

        else:
            Global.user = User()
        # self.manager.current = "ChatScreen"
        
    def login(self):
        Global.user.send_req(f'l {self.login_username_input_box.text} {kappak_hash(self.login_password_input_box.text)}')

    def account_not_found_notify(self):
        self.login_username_input_box.error_notify("Account not found")
    
    def incorrect_password_notify(self):
        self.login_password_input_box.error_notify("Password is incorrect")

    def go_to_signup_screen(self, button):
        self.manager.current = 'SignUpScreen'