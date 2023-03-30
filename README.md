# mtg-deck-generator
Generates a MtG Commander deck based on user input.

What do I want it to do?

1. Ask the user if they have a specific commander in mind.
    a. If yes, skip 3.

2. Ask the user if they have any specific cards they want to include. Either path/to/list or copy paste in the cards separated by commas.
    a. If the specific cards don't match the colour identity or are banned, return "I'm sorry, the following card(s) either aren't legal or don't match the colour identity, would you like me to remove them?"
    b. If no, say "I'm afraid I can't build a valid commander deck with this." and exit.
    c. If yes, remove them from the decklist and continue.

3. If no, ask the user if they have a specific color combination in mind.

4. Regardless of 2 or 3, ask the user if they have a specific theme in mind.
    a. i.e. spellslinger, mill, creature tribal, etc.
    b. "Please type "themes" for instructions.

5. If option picked at 1., do not ask 2.
6. If no option is picked at 1. and 2., do random.
7. If no option is picked at 3. use one of the top 3 common archetypes for chosen commander.

8. Use this card recommendation engine to build a good deck: https://github.com/donaldpminer/edhrec/blob/master/core.py

9. The deck is printed in the console.
10. Deck stats are printed in the console.
    a. i.e. %lands, %spellytypes, mana curve, etc.
