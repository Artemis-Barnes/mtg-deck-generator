#This function asks the user for information about the deck they'd like to build.
#These optioins include:
#   1. What config.commander they'd like to use.
#   2. If no config.commander is selected, what color identity they'd like to use.
#   3. If no color identity is picked, then pick a random one and pick a rasonable config.commander for that random color identity.
#   4. What cards they'd like to add to their deck.
#   5. What cards they'd like to exclude from their deck.
#   6. What theme they'd like to have their deck to have. i.e. creature tribal, control, spellslinger, mill, etc.

import random
import config

#TODO: Sanitise config.commander names after being entered.
#TODO: Add a check to see if the config.commander can be found in the database.
def user_options():
    print("\n\nWelcome to the Magic the Gathering Commander deck generator!")

    #This section asks the user to pick a deck theme. If the user types /wut then they are told how to complete this section.
    #The input is compared against a list of deck themes. If it matches one in the list, the config.deck_theme will be set to it.
    #If the deck theme is not on the list, they will be asked to try again.
    #If the deck theme is random, it will set a random deck theme.
    #If the deck theme is left blank, the generator will not look for decks of a specific theme.
    config.deck_theme_types = ["creature", "control", "mill", "landfall", "token", "voltron", "artifact"]
    while True:
        try:
            config.deck_theme = input("\nWhat theme would you like to make your deck?\nType /wut for instructions.\nType random to make a random theme.\nLeave blank and press enter for no theme.\n").strip()
            config.deck_theme.lower()
            if config.deck_theme not in config.deck_theme_types and len(config.deck_theme) != 0 and config.deck_theme != "/wut" and config.deck_theme != "random":
                raise ValueError
            if config.deck_theme == "/wut":
                config.deck_theme = input("Here, you can specify what type of themes your deck will have.\nFor now, I will accept one of the following types:\nCreature\nControl\nMill\nLandfall\nToken\nVoltron\nArtifact\nPlease enter a valid type:\n")
                config.deck_theme.lower()           
        except ValueError:
            print("I'm sorry, that is not a valid deck type. Please try again.")
            continue
        if config.deck_theme == "":
            break
        if config.deck_theme == "random":
            config.deck_theme = random.choice(config.deck_theme_types)
            break
        elif config.deck_theme in config.deck_theme_types:
            break
    if config.deck_theme == "":
        print("Okay, I won't try to make this deck a specific theme.")
    else:
        print("Okay, I'll make a " + config.deck_theme + " deck.")
    
    #This part asks the user to set a config.commander.
    #If none is picked, it will ask for a colour identity.
    #If no colour identity is picked, it will pick a random one.
    #If the config.commander picked is listed in the valid config.commander dictionary, it will set the correct colour identity
    #If the config.commander picked is NOT listed in the valid config.commander dictionary, it will set a random colour identity.
    config.commander = input("Do you have a config.commander in mind? If so, enter its name. If not, press enter.\n").strip()
    if not config.commander:
        color_identity = input("In that case, do you have a colour identity in mind? If so, enter it (e.g. WUBRG, WUBG, UBG, WR, U). If not, press enter.\nPlease keep your colors in the correct WUBRG order.\n").strip()
        if not color_identity:

            #Picks a random set of letters from the string "WUBRG" and makes it the colour identity.
            #Preserves the order of WUBRG, too. That was a pain to work out.
            random_range = random.randrange(1, 6)
            selected_colors = random.sample("WUBRG", random_range)
            color_identity = "".join(sorted(selected_colors, key="WUBRG".index))

        #Creates a dictionary that associates the letters in WUBRG with their full name.

        #Creates list that is then filled in wth the name of each colour according to its letter in the color_identity.
        #It uses each letter in the color_identity string as a key, finds its value from the color_identity_dictionary, then appends the value
        #to the empty converted_color_identity list.
        converted_color_identity = []
        for i in color_identity:
            converted_color_identity.append(config.color_identity_dictionary[i])

        #Since we can't print a list, we convert it to a string, separating the items on the list by commas.
        printed_color_identity = ", ".join(converted_color_identity)

        print("All right, I will use " + printed_color_identity + " for your deck.")        
        
        #Here I will call the card recommendation engine to find a config.commander for the right color identity.
        #For now it will just be a generically selected config.commander.
        config.commander = str("Generic " + printed_color_identity + " config.commander.")

    #TODO: Use the card recommendation engine to find and set the colour identity of the chosen config.commander, so I can delete this block:
    if config.commander in config.valid_commanders:
        color_identity = "".join(config.valid_commanders[config.commander])
        converted_color_identity = []
        for i in color_identity:
            converted_color_identity.append(config.color_identity_dictionary[i])
        printed_color_identity = ", ".join(converted_color_identity)      
    elif len(color_identity) == 0:
        random_range = random.randrange(1, 6)
        selected_colors = random.sample("WUBRG", random_range)
        color_identity = "".join(sorted(selected_colors, key="WUBRG".index))
        converted_color_identity = []
        for i in color_identity:
            converted_color_identity.append(config.color_identity_dictionary[i])
        printed_color_identity = ", ".join(converted_color_identity)

    if len(config.deck_theme) != 0:
        print("Okay, I'll make a " + printed_color_identity + " " + config.deck_theme + " deck using " + config.commander + ".")
    else:
        print("Okay, I'll make a " + printed_color_identity + " deck using " + config.commander + " with no specific theme.")

# Interacts with the card-engine module to create a deck of cards.
#def generate_deck(config.commander, colour_identity, theme):

user_options()