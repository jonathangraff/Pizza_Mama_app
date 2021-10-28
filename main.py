from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from http_client import HttpClient
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parent):
        try:
            pizzas_dict = StorageManager().load_data("pizzas")
            self.recycleView.data = pizzas_dict
        except:
            self.recycleView.data=[]

    def on_server_data(self, pizza_dict):
        self.recycleView.data = pizza_dict
        StorageManager().save_data("pizzas", pizza_dict)

    def on_server_error(self, error):
        self.error_str = error


class PizzaApp(App):
    pass


PizzaApp().run()
