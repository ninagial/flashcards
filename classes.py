from random import shuffle
import copy

class Pair(object):
    def __init__(self, a, b, tags=[]):
        self.a = a
        self.b = b
        self.tags = tags
    def __str__(self):
        return "%s -> %s" % (self.a,self.b)
    def tag(self, tag):
        self.tags.append(tag)

class Deck(object):
    def __init__(self, name="", items=[]):
        self.name = name
        self.items = items
    def __str__(self):
        if len(self.items) > 0:
            return "Deck: %s\n%s\n" % (self.name, "\n".join([str(i) for i in self.items ]))
        else:
            return "Deck: %s\nThere is nothing here!\n" % self.name
    def empty(self):
        return self.items == []
    def new(self, i):
        self.items.append(i)
    def shuffle(self):
        items_out = self.items
        shuffle(items_out)
        return Deck(name=self.name+'shuffled', items=items_out)
    def pop_item(self):
        return self.items.pop()
    def swap(self):
        return Deck(name=self.name+'_reversed', items=[Pair(x.b,x.a) for x in self.items])
    def filter_tags(self, tags):
        out = []
        for pair in self.items:
            if pair.tags != []:
                for tag in pair.tags:
                    if tag in tags:
                        out.append(pair)
        return out
    def subset(self, n, start=None):
        if start==None:
            start=0
        return Deck(name=self.name+str(n), items=self.items[start:(start+n)-1])
    def lookup(self, term):
        out = [str(p) for p in self.items if term in p.a]
        if len(out) == 0:
            return 'No matching items'
        if len(out) == 1:
            return out[0]
        return ';'.join(out)
    def practice(self, subset=False, reverse=False, shuffle=False, lookup_deck=None, start=None):
        current_deck = copy.deepcopy(self)
        revision = Deck(name='revision', items=[])
        if subset:
            current_deck = current_deck.subset(subset, start)
        if shuffle:
            current_deck = current_deck.shuffle()
        if reverse:
            current_deck = current_deck.swap()
            if lookup_deck != None:
                lookup_deck = lookup_deck.swap()

        inp = ''
        trials = 0
        correct = 0

        while (inp != 'q'):
            this = None
            if len(current_deck.items) < 1:
                break
            current = current_deck.pop_item()
            print(">>%s\n?>\n" % current.a)
            response = input()
            if response != current.b:
                this = False
                print("NO! It is: %s" % current.b)
                revision.new(current)
                print("Item added to Revision List.")
            else:
                this = True
                correct += 1
                print('YES!')
            trials += 1
            # things to do after trial
            print("Enter command or hit Return to continue...\n")
            inp = input()
            if inp == "l":
                if lookup_deck == None:
                    print(">> LOOKUP RESULT in %s: " % self.name, self.lookup(current.a))
                else:
                    print(">> LOOKUP RESULT in %s: " % lookup_deck.name, lookup_deck.lookup(current.a))
            if inp =="x":
                if not this:
                    revision.pop_item()
                else:
                    print("I don't wanna.")
            if inp == "q":
                break
        return {'trials': trials, 'correct':correct, 'score': 100*correct/trials, 'revision' : revision}
