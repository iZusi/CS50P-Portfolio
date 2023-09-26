import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
lst = ['-f', '--font']

if len(sys.argv) == 1:
    # prompt user for input
    text = input('Input: ')

    # iterate through the list of fonts in figlet and set to output
    while len(figlet.getFonts()) > 0:
        f = random.choice(figlet.getFonts())
        figlet.setFont(font = f)
        text = figlet.renderText(text)

        # display output
        print(f'Output: {text}')
        break
elif len(sys.argv) == 3:
    for f in figlet.getFonts():
        if (sys.argv[1] in lst) & (sys.argv[2] == f):
            # prompt user for input
            text = input('Input: ')

            # set font
            figlet.setFont(font = f)
            text = figlet.renderText(text)

            # display output
            print(f'Output: {text}')
            break
    if sys.argv[1] not in lst:
        sys.exit('Invalid usage')
    elif sys.argv[2] != f:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
