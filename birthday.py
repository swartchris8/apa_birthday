import pyfiglet
import random 
import time
import os

def clear_screen():
    # Function to clear the screen in cmd
    os.system('cls' if os.name == 'nt' else 'clear')

def read_ascii_art(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "ASCII art file not found."

def happy_birthday():
    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'rose', 'cyan', 'white']
    b_text = "Happy 68th Birthday Apa!"
    birthday_text = pyfiglet.figlet_format(b_text, font="slant")
    ascii_image = read_ascii_art('ascii_image.txt')
    
    while True:
        for color in colors:
            clear_screen()
            print("\033[{}m".format(random.randint(31, 37)), end='')
            print(ascii_image)
            print(birthday_text)
            print(b_text)
            print("Scroll up for the full image!")
            time.sleep(20)
            clear_screen()
            time.sleep(20)

happy_birthday()
