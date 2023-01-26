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


class Cell:
    def __init__(self, position):
        self.position = position
    
    def __hash__(self) -> int:
        return hash(self.position)

    def __eq__(self, other):
        return self.position == other.position
