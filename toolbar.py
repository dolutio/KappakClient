import Global

from kivymd.uix.floatlayout import MDFloatLayout
from sendtools import MessageInputBox, SendButton
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.button import MDIconButton
from kivy.uix.widget import Widget

class AdreesseInfo(MDTopAppBar):
    adreesse_name = 'User'
    
    def __init__():
        pass

class SideBarInputBox(MDTextField):
    mode = 'round'
    _line_color_focus = (0.5, 1.5, 0.5, 0.5)
    _line_color_normal = (0.5, 1.5, 0.5, 0.5)
    line_color_focus = (0.5, 1.5, 0.5, 1)
    line_color_normal = (0.5, 1.5, 0.5, 1)
    fill_color_normal = (0.1, 0.1, 0.2, 1)
    fill_color_focus = (0.1, 0.1, 0.2, 1)
    text_color_normal = (0.5, 1, 0.5, 1)
    text_color_focus = (0.5, 1, 0.5, 1)
    hint_text_color_normal = (0, 0.7, 0, 0.7)
    hint_text_color_focus = (0, 0.7, 0, 0.7)
    size_hint = (1, None)
    pos_hint = {'x': 0, 'y': 0}

class ChatSideBar(MDNavigationDrawer):
    md_bg_color = (0.05, 0.08, 0.12, 1)
    anchor = 'right'
    orientation = 'vertical'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.custom_key_input_box = SideBarInputBox(hint_text='Custom crypt key')
        self.custom_key_input_box.bind(text=self.on_custom_key_text_changed)

        self.add_member_input_box = SideBarInputBox(hint_text='Username')

        self.add_member_button = MDIconButton(md_bg_color=(0.1, 0.1, 0.2, 1), theme_text_color='Custom', text_color=(0.5, 1, 0.5, 1), icon='account-plus', size_hint=(1, None))
        
        self.add_widget(self.custom_key_input_box)
        self.add_widget(Widget(size_hint=(1, 0.2)))
        self.add_widget(self.add_member_input_box)
        self.add_widget(Widget(size_hint=(1, 0.05)))
        self.add_widget(self.add_member_button)
        self.add_widget(Widget())

        self.bind(state=self.on_state_change)

    def on_state_change(self, instance, state):
        if instance:
            self.custom_key_input_box.text = Global.chats_data[Global.current_chat_name]['custom_key']

    def on_custom_key_text_changed(self, instance, value):
        Global.chats_data[Global.current_chat_name]["custom_key"] = self.custom_key_input_box.text
    
    def add_member(self, button):
        if Global.user.authed:
            Global.user.send_req(f'addm {self.add_member_input_box.text}_ {Global.current_chat_name}')

class SendBar(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_input_box = MessageInputBox()
        self.send_button = SendButton()

        self.build()

    def build(self):
        self.add_widget(self.message_input_box)
        self.add_widget(self.send_button)