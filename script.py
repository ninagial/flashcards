from classes import *
from matter import *

def practice_deck(deck=japanese, reverse=False, shuffle=False, max_trials = 3, revision_deck=revision):

    if shuffle:
        deck = deck.shuffle()
    if reverse:
        deck = deck.swap()

    inp = ''
    trials = 0
    correct = 0

    while (inp != 'q'):
        if trials > max_trials:
            break
        if len(deck.items) < 1:
            break
        current = deck.pop_item()
        print(">>%s\n?>\n" % current.a)
        response = input()
        if response != current.b:
            print("NO! It is: %s" % current.b)
            revision_deck.new(current)
            print("Item added to Revision List.")
        else:
            correct += 1
            print('YES!')
        trials += 1
        inp = input()
    return {'trials': trials, 'correct':correct, 'score': correct/trials, 'revision' : revision_deck}

try0 = practice_deck(counters) 
print("This trial's score: %.2f%%\n" % try0['score'])
print(japanese_short)
print(revision)
print("LOOK UP results:\n %s" % japanese.lookup('one thing'))
