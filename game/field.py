class Field():
    '''Create field'''
    def __init__(self, width:int = 100, heigth:int = 100, bombs:int = 3000) -> None:
        self.width = width
        self.heigth = heigth
        self.bombs = width * heigth if bombs > width * heigth else bombs
        self.char = '■'
        self.char_b = 'B'
        self.char_0 = ' '
        self.field = self.generate_field()
    
    def generate_field(self) -> list:
        '''Generate field'''
        line = []
        for i in range(self.width):
            line.append(self.char)
        field = []
        for i in range(self.heigth):
            field.append(line)
        return field
    
    def generate_bombs(self):
        '''Place bombs'''
        pass
