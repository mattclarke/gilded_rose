class World:
    def __init__(self):
        self.cells = set()

    def add_cell(self, cell):
        self.cells.add(cell)

    def isempty(self):
        return len(self.cells) == 0
