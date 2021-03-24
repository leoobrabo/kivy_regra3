from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
#Config.set('graphics', 'fullscreen', 1)
# teste
#Window.size = (300, 500)


class TextFieldFocus(MDTextField, FocusBehavior):
    ...


class ButtonFocus(MDRoundFlatIconButton, FocusBehavior):
    ...


class TelaCalculo(Screen):

    def Calculo(self):
        p1 = self.ids.p1.text
        p2 = self.ids.p2.text
        p3 = self.ids.p3.text
     
        try:
            f1 = float(p1.replace(',', '.'))
            f2 = float(p3.replace(',', '.')) * float(p2.replace(',', '.'))
            f3 = f2/f1
            resultado = float(f3)

            self.ids.resultado.text = str(resultado)
        except ValueError:
            self.ids.resultado.text = 'Digite apenas numeros'

    def Limpar(self):
        self.ids.p1.text = ''
        self.ids.p2.text = ''
        self.ids.p3.text = ''
       
        self.ids.resultado.text = 'Resultado'


class Regra3(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Blue'
        #self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('design.kv')


if __name__ == '__main__':
    app = Regra3()
    #Window.fullscreen = 'auto'
    app.run()
