from kivy.core.window import Window

from kappak_config import window_height, window_width

def return_values(value, count_of_return_values):
    return tuple(value for _ in range(count_of_return_values))

def adaptive_size(value):
    return value / window_width * Window.height