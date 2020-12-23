# Flashcards Script

A Python script to practice decks of Flashcards.

# Usage

Clone the repository and navigate into the directory.

Then:

`python script.py`
	
# Adding your own material

In the file `matter.py` you will find a list of `Pair(a, b)` objects.

Modify this in order to add your own learning material.

# Options

In the file `script.py` you can select some variations of the same theme:

`practice_deck(deck=japanese, reverse=True)` : Adding `reverse=True` will present the words the other way round.
`practice_deck(deck=japanese, shuffle=True)` : Adding `shuffle=True` will present the words in random order.
`deck=something` select a deck defined in `matter.py`.
`revision_deck=something` set the revision deck, as defined in `matter.py`.
	
# Tags

`Pairs` in `matter.py` can be tagged like this:

`Pair('January', 'itsigatsu', tags = ['months'])`

It is not necessary to use _semantic_ tags. For instance `lesson 1` might come in handy, if you jsut want to organize the subject matter to more manageable sections.

Consult the code in `matter.py` for an example. This line however does that quickly, if you are font of [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

	numbers = Deck('Numbers', items = [Pair(pair.a, pair.b, tags=['numbers']) for pair in japanese.items if pair.a in ('one', 'two')])

Either way, when you have a Deck with tagged items, you can use:

	counters = Deck('Counters', items = numbers.filter_tags('counters'))
	
In order to use this as the practice deck, change line 34 in `script.py` to:

	try0 = practice_deck(counters) 
