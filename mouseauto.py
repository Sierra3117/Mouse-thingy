from pynput import keyboard
import time
import random
import pyautogui as pag

def on_press(key):
    try:
        global user_input 
        if key.char == "c":
            user_input = "c"
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def wait_for_user_input():
    global user_input
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    user_input = 0
    while user_input == 0:
        time.sleep(0.5)
        x = random.randint(900,1500)
        y = random.randint(400,800)
        pag.moveTo(x,y,0.2) 
        time.sleep(1)
        if user_input == "c":

            listener.stop()
            break

wait_for_user_input()