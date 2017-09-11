import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import *


class gridApp(App):
    def build(self):
        return GridLayout()

gApp=gridApp()
gApp.run()