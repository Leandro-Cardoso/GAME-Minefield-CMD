from field import Field

minefield = Field(10, 5, 15)
print(minefield.width, 'x', minefield.heigth)
print(minefield.bombs)
for line in minefield.field:
    print(''.join(line))
