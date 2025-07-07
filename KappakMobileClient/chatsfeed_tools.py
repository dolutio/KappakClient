from kivymd.uix.button import MDFillRoundFlatButton, MDRectangleFlatIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp

class ChatsFeedTopBar(MDTopAppBar):
    ...

class AddChatButton(MDFillRoundFlatButton):
    md_bg_color = (0, 0, 1, 1)
    md_bg_color_disabled = (0, 0, 0.5, 1)
    text_color = (1, 1, 1, 1)
    text = '+'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._round_rad = (1, 1)
        self.font_size = 60

class ChatsFeedButton(MDRectangleFlatIconButton):
    font_name = 'DejaVuSans.ttf'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.height = dp(100)