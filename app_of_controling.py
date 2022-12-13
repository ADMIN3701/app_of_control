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
        self.Label_text = ""

        al = AnchorLayout()
        bl_main = BoxLayout(orientation="horizontal", padding=25, spacing=25)
        bl1 = BoxLayout(orientation="vertical")
        bl2 = BoxLayout(orientation="vertical")

        self.text_input = TextInput(text="192.168.0.167 1234\nВведите ip адрес и порт")
        self.text_input2 = TextInput(text="Введите команду")
        self.label = Label()
        self.label2 = Label()

        self.label_split = self.label.text.split(" ")
        #self.label_split2 = self.label_split.split()

        # self.label2.text = "подключение..."
        # self.client.connect(("192.168.0.167", 1234))
        # self.label2.text = "подключено!"

        bl1.add_widget(self.label)
        bl1.add_widget(self.text_input)
        bl1.add_widget(Button(text="Подтвердить текст", on_press=self.add_operation))

        bl2.add_widget(self.label2)
        bl2.add_widget(self.text_input2)
        bl2.add_widget(Button(text="Подтвердить", on_press=self.send_command))

        bl_main.add_widget(bl1)
        bl_main.add_widget(bl2)
        al.add_widget(bl_main)
        return al

    def send_command(self, instate):
        self.label2.text = self.text_input2.text
        tttt = self.text_input2.text
        self.client.send(tttt.encode("utf-8"))


    def add_operation(self, instate):
        self.Label_text += str(self.text_input.text) + "\n"
        print(self.text_input.text)
        self.label_update()

        try:
            self.client.connect(("192.168.0.167", 12341))
            self.Label_text += "Подключено!"
        except:
            self.label.text = "Не удалось подключиться :("

    def label_update(self):
        self.label.text = self.Label_text

        # ttt = self.text_input.text
        # self.client.send(ttt.encode("utf-8"))


if __name__ == "__main__":
    MyApp().run()
