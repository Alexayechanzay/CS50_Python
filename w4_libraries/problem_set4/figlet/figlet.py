from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont()
    user_input = input('Input: ')
    print(figlet.renderText(user_input))
elif len(sys.argv) == 3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in fonts):
        user_input = input('Input: ')
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
