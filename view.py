menu_options = {
    "Quit": "x",
    "Examine an entry": "e", 
    "Filter on an feature": "f",
    "Sort on a feature": "s"
}

def print_menu_options():
    for option, command in menu_options.items():
        print(f"{option:.<30}{command}")