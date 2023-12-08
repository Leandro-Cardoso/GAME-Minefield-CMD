from random import randint

class Field():
    '''Create field.'''
    def __init__(self, rows:int = 100, cols:int = 100, bombs:int = 3000) -> None:
        self.rows = rows
        self.cols = cols
        self.bombs = rows * cols if bombs > rows * cols else bombs
        self.char = '■'
        self.char_b = 'B'
        self.char_0 = ' '
        self.field = []
    
    def generate_field(self):
        '''Generate field.'''
        for row in range(self.rows):
            cols = []
            for col in range(self.cols):
                cols.append(self.char)
            self.field.append(cols)
    
    def generate_bombs(self):
        '''Generate bombs.'''
        for bomb in range(self.bombs):
            while True:
                row = randint(0, self.rows - 1)
                col = randint(0, self.cols - 1)
                if self.field[row][col] == self.char:
                    self.field[row][col] = self.char_b
                    break

    def generate_numbers(self):
        '''Generate numbers.'''
        for row in range(self.rows):
            for col in range(self.cols):
                if self.field[row][col] != self.char_b:
                    bombs = 0
                    # TOP BOMBS:
                    if 0 <= row - 1 <= self.rows - 1:
                        if self.field[row - 1][col] == self.char_b:
                            bombs += 1
                        if 0 <= col - 1 <= self.cols - 1:
                            if self.field[row - 1][col - 1] == self.char_b:
                                bombs += 1
                        if 0 <= col + 1 <= self.cols - 1:
                            if self.field[row - 1][col + 1] == self.char_b:
                                bombs += 1
                    # MIDDLE BOMBS:
                    if 0 <= col - 1 <= self.cols - 1:
                        if self.field[row][col - 1] == self.char_b:
                            bombs += 1
                    if 0 <= col + 1 <= self.cols - 1:
                        if self.field[row][col + 1] == self.char_b:
                            bombs += 1
                    # BOTTOM BOMBS:
                    if 0 <= row + 1 <= self.rows - 1:
                        if self.field[row + 1][col] == self.char_b:
                            bombs += 1
                        if 0 <= col - 1 <= self.cols - 1:
                            if self.field[row + 1][col - 1] == self.char_b:
                                bombs += 1
                        if 0 <= col + 1 <= self.cols - 1:
                            if self.field[row + 1][col + 1] == self.char_b:
                                bombs += 1
                    self.field[row][col] = str(bombs)
