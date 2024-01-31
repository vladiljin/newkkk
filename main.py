# Import necessary modules from Kivy
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image

# Set the minimum version of Kivy required
kivy.require('1.9.0')

class BoxLayoutMain(BoxLayout):
    pass

class OverlayLayout(RelativeLayout):
    pass

class CustomSiteButton(Button):
    background_normal = StringProperty('data/sbtn1.png')
    background_down = StringProperty('data/sbtn2.png')  

    def __init__(self, **kwargs):
        super(CustomSiteButton, self).__init__(**kwargs)
        self.size_hint = (0.9, None)
        self.height = dp(38)
        self.pos_hint = {'center_x': 0.5}
        self.background_size = (self.width, self.height)  # Set background_size to stretch

class CustomExitButton(Button):
    background_normal = StringProperty('data/exit1.png')
    background_down = StringProperty('data/exit2.png')  

    def __init__(self, **kwargs):
        super(CustomExitButton, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = ('40dp', '40dp')
        self.pos_hint = {'x': 0, 'top': 1}
        self.bind(on_release=self.on_button_release)

    def on_button_release(self, *args):
        # Call the exit_confirmation method from the MyApp instance
        app_instance = App.get_running_app()
        app_instance.exit_confirmation()


class MyApp(App):
    button_height = dp(38)

    def exit_confirmation(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Do you want to exit the application?', size_hint=(1, 1)))
        btn_layout = BoxLayout()

        # Adjust button height here
        btn_yes = Button(text='Yes', size_hint=(1, 0.7))
        btn_yes.bind(on_press=self.exit_app)  # Bind the "Yes" button to exit_app method

        # Adjust button height here
        btn_no = Button(text='No', size_hint=(1, 0.7))
        btn_no.bind(on_press=self.dismiss_popup)

        btn_layout.add_widget(btn_yes)
        btn_layout.add_widget(btn_no)
        content.add_widget(btn_layout)

        self.popup = Popup(title='Exit Confirmation', content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    def exit_app(self, instance):
        self.stop()  # Stop the application

    def dismiss_popup(self, instance):
        self.popup.dismiss()

    def build(self):
        return BoxLayoutMain()


if __name__ == "__main__":
    # Create the root widget
    root = MyApp()

    # Bind the Kivy app to the root widget
    root.run()
