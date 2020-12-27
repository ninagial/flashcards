import argparse
from classes import *
from matter import *
import copy

# allow passing arguments in the command line
parser = argparse.ArgumentParser()
parser.add_argument("--deck", "-d", help="which deck to use (must exist)")
parser.add_argument("--nitems", "-n", help="number of items to practice", type=int)
parser.add_argument("--lookup", "-l", nargs=1, type=str, help="look up entry in deck")
parser.add_argument("--shuffle", action='store_true', help="shuffle the deck")
parser.add_argument("--reverse", action='store_true', help="swap the deck (terms become definitions and vice versa")
args = parser.parse_args()

try0 = decks[args.deck].practice(subset=args.nitems, max_trials=50, reverse=args.reverse, shuffle=args.shuffle)
print("This trial's score: %.2f%%\n" % try0['score'])
print(try0['revision'])

if not try0['revision'].empty():
    try1 = try0['revision'].practice()
    print("This trial's score: %.2f%%\n" % try1['score'])
    print(try1['revision'])

