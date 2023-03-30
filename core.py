#Logic order:
    #1. ask deck theme.
    #2. ask deck commander.
    #3. ask deck colour identity.
    #4. ask deck included cards.
    #5. ask deck excluded cards.
    #6. compile choices.

import random
import config

commander = config.commander
color_identity = config.color_identity
deck_theme = config.deck_theme
color_identity_dictionary = config.color_identity_dictionary
included_cards = config.included_cards
excluded_cards = config.excluded_cards
valid_commanders = config.valid_commanders

#Start with some useful functions I made.
#This one turns a colour identity code into more human readable words:
def convert_color_identity(c_id):
    converted_color_identity = []
    ordered_color_identity = "".join(sorted(c_id, key="WUBRG".index))
    for i in ordered_color_identity:
        converted_color_identity.append(config.color_identity_dictionary[i])
    human_color_identity = ", ".join(converted_color_identity)
    return human_color_identity.lower()

#This one will eventually find the colour identity of a commander:
def get_commander_color_identity(commander): #Replace this with something that actually searches a database, lol.
    if commander in valid_commanders:
        selected_colors = valid_commanders[commander]
        return selected_colors
    else:
        random_range = random.randrange(1, 6)
        selected_colors = random.sample("WUBRG", random_range)
        return selected_colors

#Now we ask users for their inputs, starting with the deck theme:
def ask_theme():
    valid_deck_theme = config.valid_deck_theme
    other_options = ["", "none"]
    valid_answers = [valid_deck_theme, other_options]
    print("\nHello, welcome to the Magic the Gathering Commander Deck generator!\nFirst, please type your deck theme and press enter. Type /list for the list of valid deck themes.\nIf you do not want a deck theme, type \"none\" and press enter.\nIf you want a random deck theme, leave it blank and press enter.")
    while True:
        deck_theme_ask = input()
        if any(deck_theme_ask in sublist for sublist in valid_answers):
            break
        elif deck_theme_ask == "/list":
            print("\nHere's a list of valid deck themes:\n" + "\n".join(valid_deck_theme) + "\n\nPlease enter one of the above:")
            continue
        else:
            print("\nI'm sorry, this is not a valid deck theme. Type /list for the list of valid deck themes or try again:")
            continue
    if deck_theme_ask == "":
        deck_theme_ask = random.choice(valid_deck_theme)
        print ("\nSure thing, I have randomly selected to make a " + deck_theme_ask + " deck.")
    elif deck_theme_ask in valid_deck_theme:
        print ("\nSure thing, I will try to create a " + deck_theme_ask + " deck.")
    elif deck_theme_ask == "none":
        deck_theme_ask = ""
        print("\nSure thing, I will not try to use a theme for your deck.")
    else:
        print("\nWhat? How did this happen?")
    return deck_theme_ask

#Now we have a deck theme, we can ask for a commander. This will spit out the commander's colour identity too.
def ask_commander():
    print("\nWhat commander would you like to use?\nType the commander's name and press enter.\nIf you don't have one in mind, leave blank and press enter.")
    commander_ask = input()
    if not commander_ask:
        print("Since you don't have one in mind, please enter a colour identity in WUBRG format.\nI will select a commander in that colour identity using the theme selected earlier.\nIf you don't have a colour identity in mind, leave it blank and press enter. I will randomly select one.")
        color_identity_ask = input()
        if not color_identity_ask:
            commander_ask = random.choice(list(valid_commanders))
            color_identity_ask = valid_commanders[commander_ask]
            print("All right, I will use " + commander_ask + " as your commander.\nIts color identity is " + convert_color_identity(color_identity_ask) + ".")
            return commander_ask, color_identity_ask
        else:
            print("Okay, I will use a " + convert_color_identity(color_identity_ask) + " commander.")
            print("I have selected Generic " + convert_color_identity(color_identity_ask) + " Commander.")
            commander_ask = str("Generic " + convert_color_identity(color_identity_ask) + " Commander")
            return commander_ask, color_identity_ask
    elif commander_ask in valid_commanders:
        color_identity_ask = valid_commanders[commander_ask]
        print("Okay, I will use " + commander_ask + "\nIts color identity is " + convert_color_identity(color_identity_ask) + ".")
        return commander_ask, color_identity_ask
    else:
        color_identity_ask = get_commander_color_identity(commander_ask)
        print("\nThis commander isn't in my database yet. I'll make up a color identity for it.\nI have decided its color identity is " + convert_color_identity(color_identity_ask) + ".")
        return commander_ask, color_identity_ask

#Now we need to ask what cards they want to include:
def ask_include_cards():
    print("\nWhat cards must be INCLUDED in your deck?\nSeparate entries with a comma and space, e.g. scion of the ur dragon, utvara hellkite, urabrask the hidden\nLeave blank and press enter if none.")
    included_cards_string = input()
    included_cards_list = included_cards_string.split(", ")
    return included_cards_list

#Now we need to ask what cards they want to exclude:
def ask_exclude_cards():
    print("\nWhat cards must be EXCLUDED in your deck?\nSeparate entries with a comma and space, e.g. sol ring, the first sliver, karn's temporal sundering\nLeave blank and press enter if none.")
    excluded_cards_string = input()
    excluded_cards_list = excluded_cards_string.split(", ")
    return excluded_cards_list

#Summarise the user's choices.
def compile_user_choices(theme, commander, color, include, exclude):
    if not theme:
        print("\nI will attempt to create a " + color + " deck with no particular theme using " + commander + " as the commander.\n\nI will include the following cards:\n" + "\n".join(include) + "\n\nI will exclude the following cards:\n" + "\n".join(exclude))
    else:
        print("\nI will attempt to create a " + color + " " + theme + " deck using " + commander + " as the commander.\n\nI will include the following cards:\n" + "\n".join(include) + "\n\nI will exclude the following cards:\n" + "\n".join(exclude))
    return 1

deck_theme_ask = ask_theme()
commander_ask, identity_ask = ask_commander()
human_identity_ask = convert_color_identity(identity_ask)
include_ask = ask_include_cards()
exclude_ask = ask_exclude_cards()
compile_user_choices(deck_theme_ask, commander_ask, human_identity_ask, include_ask, exclude_ask)