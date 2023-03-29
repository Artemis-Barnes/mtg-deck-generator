#This function asks the user for information about the deck they'd like to build.
#These optioins include:
#   1. What commander they'd like to use.
#   2. If no commander is selected, what color identity they'd like to use.
#   3. If no color identity is picked, then pick a random one and pick a rasonable commander for that random color identity.
#   4. What cards they'd like to add to their deck.
#   5. What cards they'd like to exclude from their deck.
#   6. What theme they'd like to have their deck to have. i.e. creature tribal, control, spellslinger, mill, etc.

import random
import config

#TODO: Sanitise commander names after being entered.
#TODO: Add a check to see if the commander can be found in the database.
def user_options():
    print("Welcome to the Magic the Gathering Commander deck generator!")
    deck_theme_types = ["creature", "control", "mill", "landfall", "token", "voltron"]
    while True:
        try:
            deck_theme = input("What theme would you like to make your deck? Type /wut for instructions. Type random to make a random theme. Leave blank and press enter for no theme.\n").strip()
            deck_theme.lower()
        except deck_theme not in deck_theme_types and deck_theme != "":
            print("I'm sorry, that is not a valid deck type. Please try again.")
            continue
        except deck_theme == "/wut":
            deck_theme = input("Here, you can specify what type of themes your deck will have.\nFor now, I will accept one of the following types:\nCreature\nControl\nMill\nLandfall\nToken\nVoltron\nPlease enter a valid type:")
            continue
        if deck_theme == "random":
            deck_theme = random.choice(deck_theme_types)
            break
        elif deck_theme in deck_theme_types:
            break
    print("Okay, I'll make a " + deck_theme + " deck.")
    
    commander = input("Do you have a commander in mind? If so, enter its name. If not, press enter.\n").strip()
    if not commander:
        color_identity = input("In that case, do you have a colour identity in mind? If so, enter it (e.g. WUBRG, WUBG, UBG, WR, U). If not, press enter.\nPlease keep your colors in the correct WUBRG order.\n").strip()
        if not color_identity:

            #Picks a random set of letters from the string "WUBRG" and makes it the colour identity.
            #Preserves the order of WUBRG, too. That was a pain to work out.
            random_range = random.randrange(1, 6)
            selected_colors = random.sample("WUBRG", random_range)
            color_identity = "".join(sorted(selected_colors, key="WUBRG".index))

        #Creates a dictionary that associates the letters in WUBRG with their full name.
        color_identity_dictionary = {
            "W": "White",
            "U": "Blue",
            "B": "Black",
            "R": "Red",
            "G": "Green"
        }

        #Creates list that is then filled in wth the name of each colour according to its letter in the color_identity.
        #It uses each letter in the color_identity string as a key, finds its value from the color_identity_dictionary, then appends the value
        #to the empty converted_color_identity list.
        converted_color_identity = []
        for i in color_identity:
            converted_color_identity.append(color_identity_dictionary[i])

        #Since we can't print a list, we convert it to a string, separating the items on the list by commas.
        printed_color_identity = ", ".join(converted_color_identity)

        print("All right, I will use " + printed_color_identity + " for your deck.")        
        
        #Here I will call the card recommendation engine to find a commander for the right color identity.
        #For now it will just be a generically selected commander.
        commander = str("Generic " + printed_color_identity + " commander.")

    
    print("Okay, your commander is " + commander + "!")

user_options()