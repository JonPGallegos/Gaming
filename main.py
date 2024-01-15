from pynput.mouse import Controller as mCon
import time
from statistics import mean
import mouse as click
from pynput import keyboard as kb

horizontal = [0] * 20
lean = ''
tolerance = 800
count = 0
mouse = mCon()
keyboard = kb.Controller()

def on_press(key):
    try:
        if key.char == 'e' or key.char == 'q':
            global lean
            lean = key.char
    except:
        print('Invalid Keystroke')

while (1 == 1):
    # count += 1
    # if count == 100:
    #     print('running')
    #     count = 0
    time.sleep(0.001)
    horizontal = horizontal[1:] + [mouse.position[0]]
    if click.is_pressed(button='right'):
        listener = kb.Listener(
            on_press=on_press)
        listener.start()
        while click.is_pressed(button='right'):
            time.sleep(0.001)
            horizontal = horizontal[1:] + [mouse.position[0]]
            new_list = [mouse.position[0] - x for x in horizontal]
            if mean(new_list) > tolerance and lean != 'q':

                lean = 'q'
                keyboard.press(lean)
                time.sleep(0.1)
                keyboard.release(lean)
                print(lean)
            elif mean(new_list) < -tolerance and lean != 'e':

                lean = 'e'
                keyboard.press(lean)
                time.sleep(0.1)
                keyboard.release(lean)
                print(lean)
        listener.stop()






