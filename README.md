# Flashcards Script

A Python script to practice decks of Flashcards.

# Usage

Clone the repository and navigate into the directory.

Then:

`python script.py --deck="japanese"`

`python script.py --deck="japanese" --nitems=3`

`python script.py --deck="japanese --nitems=3 --shuffle"`

`python script.py --deck="japanese" --reverse`

# Omitting early entries

You'll probably find yourself reviewing time and again the early stuff when you want to move on to new material. To ignore earlier entries, do this:


`python script.py --deck="japanese" --start=3 --nitems=3`

This will start on the fourth item and use another three items afer that. You can combine this with the other flags.


# Specifying a separate lookup Deck

Pressing `l` (as in Lama) when prompted after each trial will look up the current term in the current Deck. However, you may want to look it up in another deck. Specify this as follows:

`python script.py --deck="numbers" --lookupdeck="japanese"`

Or equivalently:

`python script.py --d="numbers" --ld="japanese"`

# After trial commands

`l` will look up the current term in the Lookup Deck.

`x` will only work after a failed trial, and remove the last term entered in the Revision Deck (eg when the trial failed because of a typo or sth).

`q` will quit the current Deck.
	
## Other Options

Adding `--reverse` will present the words the other way round.

Adding `--shuffle` will present the words in random order.



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
	
Then use `python script.py -d="counters"` as expected.

# Look up terms when not practicing

For this you have to start a python REPL, ie it is only usable in the command line.

	python
	from classes import *
	from matter import *
	
	# how you say 'unification' in Japanese??
	decks["japanese"].lookup('unification')


