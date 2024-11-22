menuOptions = {
    "Quit": "x",
    "Examine an entry": "e", 
    "Filter on an feature": "f",
    "Sort on a feature": "s",
    "Upload data(csv only)": "u",
    "Print countries": "c"
}

def print_menu_options():
    for option, command in menuOptions.items():
        print(f"{option:.<30}{command}")

def display_countries(countrySet):
    columnar_printer(countrySet, numRows=4)

def columnar_printer(data, numRows=1):
    width = 80
    columnWidth = width // numRows

    if numRows == 1:
        columnWidth = None

    def formatDatum(datum):
        # Check to see if length is at least columnWidth, otherwise left justify and pad
        return f"{str(datum)[:columnWidth]:<{columnWidth}}"
    
    row = []
    for i in data:
        if len(row) < numRows - 1:
            row.append(i)
        else:
            row.append(i)
            # print(row[0])
            result = [formatDatum(d) for d in row]
            # print(f'{row[0]:columnWidth}{row[1]:columnWidth}{row[2]:columnWidth}{row[3]:columnWidth}')
            print("".join(result))
            row.clear()
    # if the number of our countries isn't divisible by numRows, this prints out the leftovers
    for i in row:
        result = [formatDatum(d) for d in row]
        print("".join(result))