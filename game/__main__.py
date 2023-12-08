from os import system

from field import Field

system('cls')

minefield = Field(5, 10, 15)
print(minefield.rows, 'x', minefield.cols)
print(minefield.bombs)

minefield.generate_field()
minefield.generate_bombs()

for line in minefield.field:
    print(''.join(line))
