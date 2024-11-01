def plant_row_grass(length):
    i = 0
    while i < length:
        i = i + 1
        harvest()
        move(North)

def plant_row_bush(length):
    i = 0
    while i < length:
        i = i + 1
        plant(Entities.Bush)
        if can_harvest():
            harvest()
            plant(Entities.Bush)
            move(North)
        else:
            move(North)
