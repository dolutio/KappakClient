from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

class MyApp(MDApp):
    def build(self):
        # Создаем корневой ScrollView
        scroll_view = ScrollView()

        # Создаем BoxLayout для размещения виджетов
        layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Добавляем кнопки в BoxLayout
        for i in range(30):  # Создаем 30 кнопок
            btn = MDRaisedButton(
                text=f"Button {i + 1}",
                size_hint=(None, None),
                size=(dp(200), dp(200)),
            )
            layout.add_widget(btn)

        # Добавляем BoxLayout в ScrollView
        scroll_view.add_widget(layout)
        return scroll_view

if __name__ == "__main__":
    MyApp().run()

import hashlib

def hash(text, cost=1, account_creating_time=10):
    account_creating_time = str(account_creating_time)
    hash_object = hashlib.sha256()

    for i in range(cost):
        if i % 7 == 0 and i > 0:
            text = 'salt' + text + 'salt'

        if i % 16 == 0 and i > 0:
            text = kappak_hash(text, account_creating_time)

        else:
            hash_object.update(text.encode())
            text = str(hash_object.hexdigest())

    return text

def kappak_hash(text, account_creating_time='10'):
    ar = []

    for i, b in enumerate(bytes(text, 'utf-8')):
        ar.append(bin(b)[2:].zfill(8))

    hash_text = merge_bites(ar)
    hash_text_first_bite = hash_text[0]
    hash_text = hash_text[1:]

    for idx, char in enumerate(hash_text):
        if idx % 7 == 0 and idx > 0:
            hash_text = hash_text[:idx] + ('1' if char == '0' else '0') + hash_text[idx+1:] # bit = not bit

    return (hash_text_first_bite + hash_text)

def merge_bites(ar):
    s = ''
    for idx, bites in enumerate(ar): 
        if idx % 3 == 0 and idx > 0:
            bites = bites[::-1]
        
        if idx % 9 == 0 and idx > 0:
            s = bites + s
        
        s += bites
    
    s = '1' + s[1:] #The first bite is 1

    return s