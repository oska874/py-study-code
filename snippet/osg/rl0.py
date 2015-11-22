import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".pyhist")
try:
    x = readline.read_history_file(histfile)
    print(histfile)
    print(x)
except IOError,e:
    print(e)
    pass

import atexit
atexit.register(readline.write_history_file, histfile)
del os, histfile
