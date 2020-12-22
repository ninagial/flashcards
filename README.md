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
	
	
