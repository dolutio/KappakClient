from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from kappak_general_functions import return_values, adaptive_size

class DatePicker(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.days_section = DateScrollView(mode='days', on_scroll_stop=lambda scroll_widget, touch, check_children=True: self.on_chosen_day(scroll_widget, touch, check_children))
        self.months_section = DateScrollView(mode='months', on_scroll_stop=lambda scroll_widget, touch, check_children=True: self.on_chosen_month(scroll_widget, touch, check_children))
        self.years_section = DateScrollView(mode='years', on_scroll_stop=lambda scroll_widget, touch, check_children=True: self.on_chosen_year(scroll_widget, touch, check_children))

        self.day = ''
        self.month = ''
        self.year = ''

        self.build()

    def build(self):
        self.add_widget(self.days_section)
        self.add_widget(self.months_section)
        self.add_widget(self.years_section)

    def on_chosen_day(self, scroll_widget, touch, check_children):
        self.day = scroll_widget.box_layout.children[scroll_widget.scroll_y] #The child of scroll_widget is BoxLayout
    
    def on_chosen_month(self, scroll_widget, touch, check_children):
        self.month = scroll_widget.box_layout.children[scroll_widget.scroll_y]

    def on_chosen_year(self, scroll_widget, touch, check_children):
            self.year = scroll_widget.box_layout.children[scroll_widget.scroll_y]

class DateScrollView(MDScrollView):
    def __init__(self, mode, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box_layout = MDBoxLayout(orientation='vertical', adaptive_height=True, size_hint_y=None, spacing=adaptive_size(10))

        if mode == 'days':
            self.build_days()

        if mode == 'months':
            self.build_months()
        
        if mode == 'years':
            self.build_years()
    
    def build_days(self):
        for day in range(1, 32):
            self.box_layout.add_widget(DateLabel(text=f'{day}'))
    
    def build_months(self):
        for month in range(1, 13):
            self.box_layout.add_widget(DateLabel(text=f'{month}'))
    
    def build_years(self):
        for year in range(1900, 2026):
            self.box_layout.add_widget(DateLabel(text=f'{year}'))
    
    def on_scroll_move(self, touch):
        return super().on_scroll_move(touch)

class DateLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)