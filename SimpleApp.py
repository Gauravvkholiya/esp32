import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create a TextInput widget
        self.text_input = TextInput(hint_text="Enter some text")
        layout.add_widget(self.text_input)

        # Create a Button widget
        btn = Button(text="Submit")
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        # Get the text from the TextInput and print it
        entered_text = self.text_input.text
        print(f"You entered: {entered_text}")

if __name__ == '__main__':
    SimpleApp().run()

