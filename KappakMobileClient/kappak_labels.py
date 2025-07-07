from kivy.core.window import Window
from kivymd.uix.label import MDLabel

from kappak_general_functions import adaptive_size, return_values

class KappakLabel(MDLabel):
    font_name = 'DejaVuSans.ttf'
    color = (0, 0, 0, 1)

class MessageLabel(KappakLabel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (1, None)
        self.pos_hint = {'x': 0, 'y': 0}
        self.padding = return_values(adaptive_size(10), 2)
        self.valign = 'bottom'
        self.halign = 'auto'
        self.font_size = 20
        self.texture_update()

class MessageTimeLabel(KappakLabel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (1, 0.1)
        self.pos_hint = {'x': 0.75, 'y': 0}
        self.padding = return_values(adaptive_size(0), 2)
        self.font_size = 15