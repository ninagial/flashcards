from random import shuffle

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
