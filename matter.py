from classes import *

decks = {

    "japanese" : Deck('Japanese', 
            [
                Pair('one', 'ichi'),
                Pair('two', 'ni'),
                Pair('one thing', 'hitotsu'),
                Pair('two things', 'futatsu'),
                Pair('January', 'ichigachu'),
                Pair('unification', 'to-oichu')
                ]),


    "numbers" : Deck('Japanese', 
    # Construct a tagged deck - Method 1
            [
                Pair('one', 'ichi', tags=['numbers']),
                Pair('two', 'ni', ['numbers']),
                Pair('one thing', 'hitotsu', ['numbers', 'counters']),
                Pair('two things', 'futatsu', ['numbers', 'counters']),
                ]),

    # Append more decks here (python dictionary elements)
    # ...................................................
    "placeholder" : Deck("Deck Name", items = [])
} # end of decks dictionary

# Example:
# Subset a deck by tags, and add it to the dictionary
decks["counters"] : Deck('Counters', items = decks["numbers"].filter_tags('counters'))
