def harvest_and_move(direction):
    if can_harvest():
        harvest()
        move(direction)

def plant_field(item):
    plant(item)
    harvest_and_move(North)