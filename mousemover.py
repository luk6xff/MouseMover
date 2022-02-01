#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "luk6xff"
__date__   = "01.02.2022"

# Mouse and Keyboard controlers
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener as KeyboardListener
# Sleep wait
from time import sleep
import threading
import random



class MouseMover():

    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardListener(on_press=self.on_press_key,
                                         on_release=self.on_release_key)
        self.app_running = True
        self.init_keyboard()
        self.init_mouse()

    def stop_mouse_running(self):
        print("stop mouse_running")
        self.mouse_running = False

    def start_mouse_running(self):
        print("start mouse_running")
        self.mouse_running = True

    def stop_all(self):
        print("stopping all!")
        self.app_running = False
        self.keyboard.stop()

    def mouse_run(self):
        while self.app_running:
            if self.mouse_running == True:
                v = (-10, 10)
                l = lambda x : random.randint(x[0], x[1])
                # Move pointer relative to current position
                self.mouse.move(l(v), l(v))
                # Scroll a few random steps down
                self.mouse.scroll(l(v), l(v))
                sleep(1)
            else:
                sleep(1)

    def on_press_key(self, key_name):
        try:
            key_name = str(key_name).strip('\'')
            #print("key_name pressed: ", key_name)
            if key_name in self.keys:
                key_hndl = self.keys[key_name]
                key_hndl()
        except AttributeError:
            print("Special Key {} pressed".format(key_name))

    def on_release_key(self, key_name):
        key_name = str(key_name).strip('\'')
        #print("key_name {} released".format(key_name))

    def init_keyboard(self):
        self.keys = {
            'p': self.start_mouse_running,
            'w': self.stop_mouse_running,
            'q': self.stop_all
        }
        self.keyboard.start()
        #self.keyboard.join()

    def init_mouse(self):
        self.start_mouse_running()
        self.mouse_thread = threading.Thread(target=self.mouse_run)
        self.mouse_thread.start()
        self.mouse_thread.join()


if __name__ == "__main__":
    mm = MouseMover()
