from os import system

from field import Field

system('cls')

minefield = Field(10, 10, 5)
print(minefield.rows, 'x', minefield.cols)
print(minefield.bombs)

minefield.generate_field()
minefield.generate_bombs()
minefield.generate_numbers()

for row in minefield.field:
    new_row = ''
    for col in row:
        new_row += col + ' ' * 2
    print(new_row)
