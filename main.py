from pynput.mouse import Button, Controller
import time
import keyboard
mouse = Controller()
i = 1


while i < 6:  # making a loopa
    print("working")
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break