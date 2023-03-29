import random
import config

print("\n\nWelcome to the Magic the Gathering Commander deck generator!")
deck_theme_types = ["creature", "control", "mill", "landfall", "token", "voltron"]
deck_theme = ""
while True:
    try:
        deck_theme = input("What theme would you like to make your deck?\nType /wut for instructions.\nType random to make a random theme.\nLeave blank and press enter for no theme.\n").strip()
        deck_theme.lower()
        if deck_theme not in deck_theme_types and len(deck_theme) != 0 and deck_theme != "/wut" and deck_theme != "random":
            raise ValueError
        if deck_theme == "/wut":
            deck_theme = input("Here, you can specify what type of themes your deck will have.\nFor now, I will accept one of the following types:\nCreature\nControl\nMill\nLandfall\nToken\nVoltron\nPlease enter a valid type:\n")           
    except ValueError:
        print("I'm sorry, that is not a valid deck type. Please try again.")
        continue
    if deck_theme == "":
        break
    if deck_theme == "random":
        deck_theme = random.choice(deck_theme_types)
        break
    elif deck_theme in deck_theme_types:
        break
if deck_theme == "":
    print("Okay, I won't try to make this deck a specific theme.")
else:
    print("Okay, I'll make a " + deck_theme + " deck.")