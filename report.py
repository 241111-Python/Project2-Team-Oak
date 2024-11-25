# Generate the standard report
def entry_formatter(name: str, length: int) -> str:
    str_length = length - 2
    if len(name) > str_length:
        return f"{name[:str_length - 2]}.."
    return f"{name:<{str_length}}"

def format_row(data, widths) -> str:
    result = ""
    data_formatted = [entry_formatter(d, w) for d, w in zip(data, widths)]
    for d in data_formatted:
        result += f"| {d} "
    result += "|\n"
    return result

def generate_divider(column_widths):
    return "-" * (len(column_widths) + sum(column_widths) + 1) + "\n"

def generate_header(column_names: list[str], column_widths: list[int]) -> str:
    horizontal_divider = generate_divider(column_widths)
    # adjust the column widths given to have as many entries as column names
    for i in range(len(column_widths), len(column_names)):
        column_widths.append(10)
    return format_row(column_names, column_widths)

def generate_data(data: list[list], column_widths: list[int]) -> str:
    return "".join([format_row(d, column_widths) for d in data])

def generate_report(names, data, widths):
    divider = generate_divider(widths)

    result = ""
    result += divider
    result += generate_header(names, widths)
    result += divider
    result += generate_data(data, widths)
    result += divider

    return result

if __name__ == "__main__":
    names = ["abc", "a really long name", "databbb"]
    data = [["abc", "123", "do rae mi"], ["led zeppelin", "ACDC", "Turgoth"]]
    widths = [6, 10, 7]
    print(generate_report(names, data, widths))