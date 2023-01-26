from world import World


def test_create_world_and_check_is_empty():
    world = World()
    assert world.isempty()


def test_add_one_cell_to_the_world():
    world = World()
    world.add_cell((0, 0))
    assert not world.isempty()


#def test_create_cell_and_check_exists():
#    cell = (1, 1)
  
