class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return "%s -> %s" % (self.a,self.b)

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
        shuffle(self.items)
    def pop_item(self):
        return self.items.pop()
    def swap(self):
        self.items = [Pair(x.b,x.a) for x in self.items]
