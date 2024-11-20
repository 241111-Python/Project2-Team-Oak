menu_options = {
    "Quit": "x"
}

def print_menu_options():
    for option, command in menu_options.items():
        print(f"{option:.<30}{command}")