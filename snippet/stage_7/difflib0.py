# -*- coding: utf-8 -*-

import difflib,sys,keyword

s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

for line in difflib.context_diff(s1,s2):
    sys.stdout.write(line)

ge = difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'],4,0.8)
print(ge)

ge = difflib.get_close_matches('wheel',keyword.kwlist) #keyword list
print(ge)

ge = difflib.ndiff('one\ntwo\nthree\n'.splitlines(1),'ore\ntree\nemu\n'.splitlines(1))
print''.join(ge)
