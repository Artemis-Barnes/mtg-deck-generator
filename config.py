import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


#These are global variables that will need to be sahred with all modules.
mana_colors = "WUBRG"
commander = ""
color_identity = ""
deck_theme = ""
included_cards = []
excluded_cards = []
valid_deck_theme = ["creature", "control", "mill", "landfall", "token", "voltron", "artifact"]
valid_commanders = {
    "Vrondiss, Rage of Ancients" : "RG",
    "Omnath, Locus of Mana" : "G",
    "Scion of the Ur Dragon" : "WUBRG",
    "Wilhelt the Rotcleaver" : "UB",
    "Aesi, Tyrant of Gyre Strait" : "UG"
}
color_identity_dictionary = {
            "W": "White",
            "U": "Blue",
            "B": "Black",
            "R": "Red",
            "G": "Green"
        }