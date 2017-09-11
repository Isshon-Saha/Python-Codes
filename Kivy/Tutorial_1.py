import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

class hello_Kivy(App):
    def build(self):
        return Label()

HelloKivy=hello_Kivy()
HelloKivy.run()