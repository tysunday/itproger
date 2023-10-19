from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Container(BoxLayout):
    text_input = ObjectProperty
    label_text = ObjectProperty

    def change_something(self):
        self.label_text.text = self.text_input.text

class DuckyApp(App):
    def build(self):
        return Container()

if __name__ == "__main__":
    DuckyApp().run()