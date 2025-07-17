import Global

from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.widget import MDAdaptiveWidget

from kivy.core.window import Window
from kivy.metrics import dp

from kappak_labels import MessageLabel, MessageUsernameLabel, MessageTimeLabel
from kappak_general_functions import return_values, adaptive_size
from kappak_config import OWN_MESSAGE, OTHER_MESSAGE

censorship_dict = {'Kill': 'K!ll', 'kill': 'k!ll', 'Die': 'D!e', 'die': 'd!e', 'Hate': 'H@te', 'hate': 'h@te', 'Stupid': 'Stup!d', 'stupid': 'stup!d'}

class Message:
    text: str
    sending_time: str
    message_id: str

    def __init__(self, text='', sending_time='0', message_id=getattr(Global.user, 'username', 'noname') + str(getattr(Global.user, 'the_last_sended_message_id', 0))):
        self.text = text
        self.sending_time = sending_time
        self.message_id = message_id
    
    def serializate(self):
        serialization_array = []
        obj_var_types = ''

        for var_value in self.__dict__.values():
            var_value_type = type(var_value)

            if var_value_type is int:
                obj_var_types += 'i'
            elif var_value_type is float:
                obj_var_types += 'f'
            elif var_value_type is str:
                obj_var_types += 'c'

            serialization_array.append(var_value)
        
        serialization_array.insert(0, obj_var_types)

        return serialization_array

class MessageWidget(MDCard):
    OWN_MESSAGE_COLOR = (0.5, 1, 0.5, 1)
    OTHERS_MESSAGE_COLOR = (0, 0.77, 0.77, 1)

    size_hint = (0.4, None)
    pos_hint = {'x': 0.5, 'y': 1}
    orientation = 'vertical'
    adaptive_height = True
    radius = return_values(dp(15), 4)
    
    def __init__(self, message=Message("HEllo"), **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.OWN_MESSAGE_COLOR

        self.message = message
        self.define_message_type()
        self.set_message_text()
        self.set_message_time()
    
    def define_message_type(self): #Own message or Someone else's message
        if Global.user.username not in self.message.message_id:
            self.md_bg_color = self.OTHERS_MESSAGE_COLOR #00c5c3 #2079df #4a5ce9 #8620df
            self.pos_hint = {'x': 0.05, 'y': 1}

            self.set_message_username()

    def censore(self, text: str):
        for word in censorship_dict:
            if word in text:
                text = text.replace(word, censorship_dict[word])

        return text
    
    def set_message_username(self):
        self.username_label = MessageUsernameLabel(text='_'.join(self.message.message_id.split('_')[:-1]))

        self.add_widget(self.username_label)
    
    def set_message_text(self):
        self.message_label = MessageLabel()
        self.message_label.text = self.censore(self.message.text)

        self.message_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.message_label.bind(texture_size=lambda instance, value: setattr(self, 'height', value[1] + adaptive_size(30)))

        self.add_widget(self.message_label)
    
    def set_message_time(self):
        sending_time_in_hours_and_minutes = self.filter_sending_time()
        self.message_time_label = MessageTimeLabel(text=str(sending_time_in_hours_and_minutes))

        self.add_widget(self.message_time_label)
    
    def filter_sending_time(self):
        time = self.message.sending_time.split(':')[3:] # "dd:mm:yy:HH:MM" -> ['dd', 'mm', 'HH', 'MM'] (mm is months, MM is minutes)

        return ':'.join(time)

class MessagesShowPlace(MDScrollView):
    size_hint = (1, 1)
    pos_hint = {'x': 0, 'y': 0}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scroll_view_layout = MDBoxLayout(orientation='vertical', adaptive_height=True, size_hint_y=None, spacing=adaptive_size(10))
        self.scroll_view_layout.pos_hint = {'x': 0.5, 'y': 0.5}

        self.spacing_widget = MDAdaptiveWidget(size_hint=(1, None))

        # self.message = MessageWidget(message=Message(text="Բարիգուն"))

        # self.message1 = MessageWidget(message=Message(text='Hello, my name is Bob, i am 10 ages old, hello, my name is Bob, i am 10 ages old'*5, message_id='Bob:1'))

        # self.scroll_view_layout.add_widget(self.message)
        # self.scroll_view_layout.add_widget(self.message1)

        self.scroll_view_layout.add_widget(self.spacing_widget)

        self.add_widget(self.scroll_view_layout)

        self.scroll_y = 0 #Scrolling down
    
    def add_message(self, message: Message):
        self.scroll_view_layout.remove_widget(self.spacing_widget)
        self.scroll_view_layout.add_widget(MessageWidget(message=message))
        self.scroll_view_layout.add_widget(self.spacing_widget)

        self.scroll_y = 0