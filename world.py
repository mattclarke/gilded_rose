class World:
    def __init__(self):
        self.cells = set()

    def add_cell(self, cell):
        self.cells.add(cell)

    def is_empty(self):
        return len(self.cells) == 0

    def is_cell_alive(self, cell):
        return cell in self.cells

    def get_num_of_neighbours(self, cell):
        pass
