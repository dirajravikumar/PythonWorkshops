from kivy.app import App
from kivy.lang import Builder


class GreetGuido(App):
    def build(self):
        self.title = "Intermediate Excercise 1"
        self.root = Builder.load_file('ie1.kv')
        return self.root

    def clear_fields(self):
        self.root.ids.input1.text = ''

    def handle_greet(self):
        self.root.ids.label1.text = 'Hello ' + self.root.ids.input1.text

GreetGuido().run()
