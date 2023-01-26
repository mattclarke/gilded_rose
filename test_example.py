from world import World, Cell


def test_create_world_and_check_is_empty():
    world = World()
    assert world.is_empty()

def test_add_one_cell_to_the_world():
    world = World()
    cell = Cell((0, 0))
    world.add_cell(cell)
    assert not world.is_empty()

def test_create_cell_and_check_exists():
    world = World()
    cell = Cell((0, 0))
    world.add_cell(cell)
    assert world.is_cell_alive(cell)

def test_check_if_cell_does_not_exist():
    world = World()
    cell = Cell((0, 0))
    assert not world.is_cell_alive(cell)

# def test_can_get_number_of_neighbours():
#     world = World()
#     cell = (0, 0)
#     assert world.get_num_of_neighbours(cell) == 0

def test_create_cell():
    cell = Cell((0, 0))
    assert cell.position == (0, 0)

def test_cells_with_the_same_position_are_the_same():
    cell_1 = Cell((0, 0))
    cell_2 = Cell((0, 0))
    assert cell_1 == cell_2

def test_duplicated_cell_is_not_added_to_world():
    pass
    # to do!!
