from classes import *

japanese = Deck('Japanese', 
        [
            Pair('one', 'ichi'),
            Pair('two', 'ni'),
            Pair('one thing', 'hitotsu'),
            Pair('two things', 'futatsu'),
            Pair('January', 'ichigachu'),
            Pair('unification', 'to-oichu')
            ])

revision = Deck('Revision')

# Construct a tagged deck - Method 1

numbers = Deck('Japanese', 
        [
            Pair('one', 'ichi', tags=['numbers']),
            Pair('two', 'ni', ['numbers']),
            Pair('one thing', 'hitotsu', ['numbers', 'counters']),
            Pair('two things', 'futatsu', ['numbers', 'counters']),
            ])
        
# Subset this, if you only need the counters

counters = Deck('Counters', items = numbers.filter_tags('counters'))

japanese_short = japanese.subset(3)
japanese_short = japanese_short.shuffle()

