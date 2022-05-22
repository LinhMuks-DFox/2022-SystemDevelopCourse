# Pragma region Constants
import random
PIECE_BUTTON_DEFAULT_STYLE_SHEET = "background-color: light gray;"
PIECE_BUTTON_BLACK_STYLE_SHEET = "background-color: black; color: white"  # set font color to white
PIECE_BUTTON_WHITE_STYLE_SHEET = "background-color: white; color: black"
PIECE_BUTTON_VALID_PLACE_STYLE_SHEET = "background-color: #66CCFF; color: valid"

def get_next_valid_place_random_style():
    color_list = ["blue", "red", "green"]
    return f"background-color: {random.choice(color_list)}; color: valid"

DEBUG = True