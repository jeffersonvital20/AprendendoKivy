from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botao 1')
        label = Label(text='oiiii')
        box.add_widget(button)
        box.add_widget(label)

        box2 = BoxLayout()
        button2 = Button(text='Incrementar', font_size=22, on_release=self.incrementar)
        self.label2 = Label(text='1', font_size=22)
        box2.add_widget(button2)
        box2.add_widget(self.label2)

        box.add_widget(box2)

        return box

    def incrementar(self, button):
        self.label2.text = str(int(self.label2.text)+1)


Teste().run()
