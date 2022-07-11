from pynput.mouse import Button, Controller
import time
from pynput import keyboard
mouse = Controller()

def on_press(key):
    try:
        print('{0}'.format(
            key.char))
    except AttributeError:
        print('{0}'.format(
            key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()