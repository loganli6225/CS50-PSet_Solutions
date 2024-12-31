import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font = list[random.randint(0, len(list)-1)])
    print(figlet.renderText(text))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            index = list.index(sys.argv[2])
        except ValueError:
            sys.exit("Invalid usage")
        else:
            text = input("Input: ")
            figlet.setFont(font = list[index])
            print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
