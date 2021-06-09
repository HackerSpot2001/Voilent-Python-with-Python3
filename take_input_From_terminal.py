#! /usr/bin/python3
import sys 

usage = "python3 take_input_From_terminal.py say_anything"
if len(sys.argv) != 2:
    print(usage)
    sys.exit()
else:
    text = sys.argv[1]
    print(text)
