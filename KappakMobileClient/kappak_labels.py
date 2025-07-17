from kivy.core.window import Window
from kivymd.uix.label import MDLabel

from kappak_general_functions import adaptive_size, return_values
from kivy.metrics import dp
from kivy.core.window import Window

class KappakLabel(MDLabel):
    font_name = 'DejaVuSans.ttf'
    color = (0, 0, 0, 1)

class MessageLabel(KappakLabel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (1, None)
        self.pos_hint = {'x': 0, 'y': 0}
        self.padding = return_values(dp(10), 2)
        self.valign = 'bottom'
        self.halign = 'auto'
        self.font_size = dp(17)
        self.texture_update()

class MessageUsernameLabel(KappakLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.5, 0.1)
        self.pos_hint = {'x': 0, 'y': 0}
        self.padding = dp(10), dp(30), dp(20), dp(20)
        self.font_size = dp(15)
        self.color = (0, 1, 0, 1)

        # Window

class MessageTimeLabel(KappakLabel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (0.5, 0.1)
        self.pos_hint = {'x': 0.75, 'y': 0}
        self.padding = dp(10)
        self.font_size = dp(15)

        Window.bind(size=self.set_pos_hint_for_phones)
        self.set_pos_hint_for_phones(None, Window.size)

    def set_pos_hint_for_phones(self, instance, size):
        if size[0] <= dp(320):
            self.pos_hint['x'] = 0.3
        
        elif size[0] <= dp(335):
            self.pos_hint['x'] = 0.45

        elif size[0] <= dp(521):
            self.pos_hint['x'] = 0.6
        
        elif size[0] <= dp(578):
            self.pos_hint['x'] = 0.7
        
        else:
            self.pos_hint['x'] = 0.75