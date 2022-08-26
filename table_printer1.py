tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def table_printer(table):
    length_list = [len(element) for row in table for element in row]
    column_width = max(length_list)

    tableprint = ''
    for row in table:
        row = "".join(element.rjust(column_width + 2) for element in row)
        tableprint += row + '\n'

    return tableprint

print(table_printer(tableData))