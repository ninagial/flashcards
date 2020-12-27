# Flashcards Script

A Python script to practice decks of Flashcards.

# Usage

Clone the repository and navigate into the directory.

Then:

`python script.py --deck="japanese"`
`python script.py --deck="japanese" --nitems=3`
`python script.py --deck="japanese --nitems=3 --shuffle"`
`python script.py --deck="japanese" --reverse`
	
## Options

Adding `--reverse` will present the words the other way round.
Adding `--shuffle` will present the words in random order.
`--deck="something"` select an existing deck defined in `matter.py`.
`--nitems` will use a subset of the deck, of the given length

# Adding your own material

Right now, you have to do this manually.

In the file `matter.py` you will find a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp) named `decks`.

In each Deck you will find a list of `Pair(a, b)` objects.

Modify this in order to add your own learning material.

	
# Tags

`Pairs` in `matter.py` can be tagged like this:

`Pair('January', 'itsigatsu', tags = ['months'])`

It is not necessary to use _semantic_ tags. For instance `lesson 1` might come in handy, if you jsut want to organize the subject matter to more manageable sections.

Consult the code in `matter.py` for an example. This line however does that quickly, if you are font of [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

	decks["numbers"] = Deck('Numbers', items = [Pair(pair.a, pair.b, tags=['numbers']) for pair in decks["japanese"].items if pair.a in ('one', 'two')])

Either way, when you have a Deck with tagged items, you can use:

	decks["counters"] = Deck('Counters', items = decks["numbers"].filter_tags('counters'))
	
In order to use this as the practice deck, change line 34 in `script.py` to:

	try0 = counters.practice() 
	
# Look up

For this you have to start a python REPL, ie it is only usable in the command line.

	python
	from classes import *
	from matter import *
	
	# how you say 'unification' in Japanese??
	decks["japanese"].lookup('unification')


