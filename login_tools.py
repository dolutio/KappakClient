from kivymd.uix.button import MDFillRoundFlatButton, MDTextButton
from kivymd.uix.textfield import MDTextField

from kappak_general_functions import return_values, adaptive_size

class AuthInputBox(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_name = 'DejaVuSans.ttf'
        self.size_hint = (0.8, 0.1)
        self.anim_rect = lambda x, y: ...
        self.background_color = (1, 1, 1, 1)

        self.line_default_color = (0.5, 1, 0.5, 1)
        self.text_default_color = (0, 1, 0, 1)

        self.line_err_color = (0.7, 0, 0, 1)
        self.text_err_color = (1, 0, 0, 1)

        self.set_colors()
    
    def error_notify(self, err_text: str):
        self.line_color_normal = self.line_err_color
        self._line_color_focus = self.line_err_color # self.line_color_focus does'nt work anytime
        self.hint_text_color_normal = self.text_err_color
        self.hint_text_color_focus = self.text_err_color
        self.text_color_focus = self.text_err_color
        self.text_color_normal = self.text_err_color
        self.hint_text = err_text

    def set_colors(self):
        self.hint_text_color_normal = self.text_default_color
        self.line_color_normal = self.line_default_color
        self.hint_text_color_focus = self.text_default_color
        self.text_color_focus = self.text_default_color
        self.text_color_normal = self.text_default_color
        self.line_color_focus = self.line_default_color
        self._line_color_focus = self.line_default_color # self.line_color_focus does'nt work anytime

    def on_text(self, instance, value):
        self.set_colors()

class AuthUserNameInputBox(AuthInputBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_name = 'DejaVuSans.ttf'
        self.hint_text = 'Username'
        self.pos_hint = {'x': 0.1, 'y': 0.8}

class AuthPassWordInputBox(AuthInputBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_name = 'DejaVuSans.ttf'
        self.hint_text = 'Password'
        self.password = True
        self.pos_hint = {'x': 0.1, 'y': 0.65}

class AuthButton(MDFillRoundFlatButton):
    text = 'SignUp'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_name = 'DejaVuSans.ttf'
        self.md_bg_color = (0.0, 0.35, 0.62, 1)
        self.size_hint = (0.1, 0.1)
        self.pos_hint = {'x': 0.45, 'y': 0.45}

class GoToAuthScreenButton(MDTextButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_name = 'DejaVuSans.ttf'
        self.color = (1, 1, 1, 1)
        self.size_hint = (0.5, 0.1)
        self.pos_hint = {'x': 0.6, 'y': 0.3}