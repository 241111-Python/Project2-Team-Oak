menu_options = {
    "Quit": "x",
    "Examine an entry": "e", 
    "Filter on an feature": "f",
    "Sort on a feature": "s"
}

def print_menu_options():
    for option, command in menu_options.items():
        print(f"{option:.<30}{command}")

def displayCountries(burgerSet):
    lst = list(burgerSet)
    lst.sort()
    row = []
    for i in lst:
        if len(row) < 3:
            row.append(i)
        else:
            row.append(i)
            print(f'{row[0]:21}{row[1]:21}{row[2]:21}{row[3]:21}')
            row.clear()
    # if the number of our countries isn't divisible by 4, this prints out the leftovers
    for i in row:
        print(f'{i:21}', end="")