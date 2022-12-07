import socket
import os
import time


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.core.window import Window
Window.size = (300, 500)

class MyApp(App):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def build(self):

        al = AnchorLayout()
        bl = BoxLayout(orientation="vertical", padding=25, spacing=25)
        self.text_input = TextInput(text="Введите текст...")
        self.label = Label()
        self.label2 = Label()


        bl.add_widget(self.label2)
        self.label2.text = "подключение..."
        self.client.connect(("192.168.0.167", 1234))
        self.label2.text = "подключено!"

        bl.add_widget(self.label)
        bl.add_widget(self.text_input)
        bl.add_widget(Button(text="Подтвердить текст", on_press=self.add_operation))

        al.add_widget(bl)
        return al

    def add_operation(self, instate):
        self.label.text = self.text_input.text
        print(self.text_input.text)

        ttt = self.text_input.text
        self.client.send(ttt.encode("utf-8"))


if __name__ == "__main__":
    MyApp().run()
