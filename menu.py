# coding: utf-8
from kivy.uix.boxlayout import BoxLayout


class Menu(BoxLayout):

    def switch_content(self, content):
        self.parent.active_content = content
