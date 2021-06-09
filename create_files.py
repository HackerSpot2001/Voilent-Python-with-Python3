import os
from random import randrange

login = os.getlogin()
while True:
    randintiger= randrange(10,10000000)
    os.mkdir(f"C:/Users/{login}/Desktop/{randintiger}")