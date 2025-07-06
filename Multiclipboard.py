# could add more features like deleting things and somehow allowing strings that you enter to have spaces and in general make this more user friendly... although could also get rid of the adding your own words option bc what is the point this isn't a notes app

import shelve
import pyperclip
import sys

shelf = shelve.open('multiclipboard')

# sys.argv[0] is always the script name (Multiclipboard.py)
if len(sys.argv) == 4 and sys.argv[1] == 'save':
    shelf[sys.argv[2]] = sys.argv[3]
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        print(list(shelf.keys()))
    elif sys.argv[1] in shelf:
        pyperclip.copy(shelf[sys.argv[1]])
    else:
        print('not in shelf')

shelf.close()