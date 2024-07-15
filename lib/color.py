import sys

if sys.platform.startswith("win"):
    red = ""
    green = ""
    reset = ""
else :
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"
    
def print_color_red(color, panle, text):
    global red, reset
    print(red + panle + text + reset)
    
def print_color_green(color, panle, text):
    global green, reset
    print(green + panle + text + reset)
