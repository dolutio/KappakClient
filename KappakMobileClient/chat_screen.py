import Global

from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout

from toolbar import ChatSideBar, SendBar
from message_tools import Message, MessagesShowPlace

class ChatScreen(MDScreen):
    name = "ChatScreen"

    size_hint = (1, 1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.md_bg_color = (0.05, 0.08, 0.12, 1)

        self.layout = MDFloatLayout()
        self.chat_side_bar = ChatSideBar()

        self.message_show_place = MessagesShowPlace(size_hint=(1, 1))
        self.send_bar = SendBar(size_hint=(1, 0.1))

        self.build()
    
    def on_parent(self, widget, parent):
        if parent:
            Global.messages_show_place_widget = self.message_show_place
            Global.message_input_box = self.send_bar.message_input_box
    
    def build(self):
        self.clear_widgets()

        for msg_id, msg in Global.chats_data[self.name].items():
            if msg_id not in ["last_received_msg_id", "custom_key"]:
                self.message_show_place.add_message(Message(msg['text'], msg['sending_time'], msg_id))

        self.layout.add_widget(self.message_show_place)
        self.layout.add_widget(self.send_bar)

        self.add_widget(self.layout)
        self.add_widget(self.chat_side_bar)