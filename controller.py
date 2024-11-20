import sys

def handle_user_input(user_selection: str):
    if user_selection == "x":
        exit_game()

def exit_game():
    sys.exit(0)