from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

from chatsfeed_tools import ChatsFeedTopBar, AddChatButton, ChatsFeedButton
from chat_screen import ChatScreen
from kappak_general_functions import adaptive_size

import json
import Global

class ChatsFeedScreen(MDScreen):
    name = "ChatsFeed"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.float_layout = MDFloatLayout()
        self.scroll_view = MDScrollView(size_hint=(1, 1))
        self.box_layout = MDBoxLayout(orientation='vertical', adaptive_height=True, size_hint_y=None, spacing=adaptive_size(10))

    def on_parent(self, widget, parent): # if widget has parent (calling when widget adding / removing)
        if parent:
            self.build_chat_buttons()

            self.scroll_view.add_widget(self.box_layout)
            self.float_layout.add_widget(AddChatButton())
            # self.float_layout.add_widget(self.box_layout)
            # self.scroll_view.add_widget(self.float_layout)
            self.add_widget(self.scroll_view)
            self.add_widget(self.float_layout)

    def create_chat_button(self, chat_name: str, index):
        self.box_layout.add_widget(ChatsFeedButton(text=chat_name, on_release=self.chats_feed_button_on_release))
        self.manager.add_widget(ChatScreen(name=chat_name))
    
    def build_chat_buttons(self):
        index = 0
        for chat_name in Global.chats_data.keys():
            self.create_chat_button(chat_name, index)
            index += 1

    def chats_feed_button_on_release(self, button):
        Global.current_chat_name = button.text
        self.manager.current = button.text