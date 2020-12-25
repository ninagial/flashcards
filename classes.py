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
    def subset(self, n):
        return Deck(name=self.name+str(n), items=self.items[:(n-1)])
    def lookup(self, term):
        out = [str(p) for p in self.items if term in p.a]
        if len(out) == 0:
            return 'No matching items'
        if len(out) == 1:
            return out[0]
        return ';'.join(out)
    def practice(self, subset=False, reverse=False, shuffle=False, max_trials = 3):
        current_deck = copy.deepcopy(self)
        revision = Deck(name='revision', items=[])

        if shuffle:
            current_deck = current_deck.shuffle()
        if subset:
            current_deck = current_deck.subset(subset)
        if reverse:
            current_deck = current_deck.swap()

        inp = ''
        trials = 0
        correct = 0

        while (inp != 'q'):
            if trials > max_trials:
                break
            if len(current_deck.items) < 1:
                break
            current = current_deck.pop_item()
            print(">>%s\n?>\n" % current.a)
            response = input()
            if response != current.b:
                print("NO! It is: %s" % current.b)
                revision.new(current)
                print("Item added to Revision List.")
            else:
                correct += 1
                print('YES!')
            trials += 1
            inp = input()
        return {'trials': trials, 'correct':correct, 'score': 100*correct/trials, 'revision' : revision}
