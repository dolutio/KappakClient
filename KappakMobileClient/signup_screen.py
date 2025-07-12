from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.pickers import MDDatePicker
from login_tools import AuthUserNameInputBox, AuthPassWordInputBox, AuthButton, GoToAuthScreenButton

from kappak_crypt import kappak_hash
from kappak_user import User

import json
import Global

class SignUpScreen(MDScreen):
    name = "SignUpScreen"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.md_bg_color = (0.05, 0.08, 0.12, 1)

        self.box = MDFloatLayout()

        self.signup_username_input_box = AuthUserNameInputBox()
        self.signup_password_input_box = AuthPassWordInputBox()

        self.saved_username = ''

        self.signup_button = AuthButton(on_release=self.signup)

        self.go_to_login_screen_button = GoToAuthScreenButton(text='Already have an account? Log In', on_release=self.go_to_login_screen)

        self.build()
    
    def on_parent(self, widget, parent):
        if parent:
            if Global.user.signed_up:
                self.manager.current = 'ChatsFeed'

    def build(self):
        self.box.add_widget(self.signup_username_input_box)
        self.box.add_widget(self.signup_password_input_box)
        self.box.add_widget(self.signup_button)
        self.box.add_widget(self.go_to_login_screen_button)
        # self.box.add_widget(MDDatePicker(size_hint=(0.8, 0.8)))

        self.add_widget(self.box)
    
    def get_user_data(self):
        try:
            with open("user_data.json", 'r') as user_data_file:
                user_data = json.load(user_data_file)
        
        except FileNotFoundError:
            user_data = None
        
        return user_data
    
    def setup_user(self):
        ...
        
    def signup(self, button):
        self.saved_username = self.signup_username_input_box.text + '_'
        self.saved_pwd_hash = kappak_hash(self.signup_password_input_box.text)
        Global.user.send_req(f'signup {self.saved_username} {self.saved_pwd_hash}')

    def account_is_already_notify(self):
        self.signup_username_input_box.error_notify("Account is already exist")
        self.signup_password_input_box.error_notify("Account is already exist")

    def save_account_data(self):
        if not Global.user.signed_up:
            Global.user.username = self.saved_username
            Global.user.pwd_hash = self.saved_pwd_hash
            Global.user.signed_up = True

    def go_to_login_screen(self, button):
        self.manager.current = "LogInScreen"