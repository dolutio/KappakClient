from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp

class ChatsFeedTopBar(MDTopAppBar):
    ...

class AddChatButton(MDIconButton):
    md_bg_color = (0, 0, 1, 1)
    md_bg_color_disabled = (0, 0, 0.5, 1)
    theme_icon_color = 'Custom'
    icon_color = (1, 1, 1, 1)
    icon = 'plus'
    icon_size = dp(70)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._round_rad = (1, 1)
        self.font_size = 60

class ChatsFeedButton(MDRectangleFlatIconButton):
    font_name = 'DejaVuSans.ttf'
    md_bg_color = (0.05, 0.08, 0.12, 1)
    line_color = (0.3, 1, 0.3, 1)
    icon_color = (0.1, 1, 0.1, 0)
    text_color = (0.1, 1, 0.1, 1)

    def __init__(self, step, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.7)
        self.pos = (0, dp(self.height - step * self.size_hint[1]))