from world import World


def test_create_world_and_check_is_empty():
    world = World()

    assert len(world.cells) == 0

#def test_create_cell_and_check_exists():
#    cell = (1, 1)
  
