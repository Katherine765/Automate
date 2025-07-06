# could add more features like deleting things

import shelve
import pyperclip
import sys

shelf = shelve.open('multiclipboard')

# sys.argv[0] is always the script name (Multiclipboard.py)
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