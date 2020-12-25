from classes import *
from matter import *

try0 = japanese.practice(subset=2, shuffle=True, reverse=False) 
print("This trial's score: %.2f%%\n" % try0['score'])
print(try0['revision'])

# Look up sth - works only inside a python REPL
print("LOOK UP results:\n %s" % japanese.lookup('one thing'))
