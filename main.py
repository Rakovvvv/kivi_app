from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a text input widget
        self.text_input = TextInput()

        # Create a button widget
        self.button = Button(text='Click me!')

        # Add the widgets to the layout
        self.add_widget(self.text_input)
        self.add_widget(self.button)

        # Bind the button to a function
        self.button.bind(on_press=self.on_button_press)

    def on_button_press(self, instance):
        # Get the text from the input widget
        text = self.text_input.text

        # Do something with the text (replace with your own code)
        print(f'The text inputted was: {text}')

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()