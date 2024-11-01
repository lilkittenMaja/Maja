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

def plant_row_carrot(length):
    i = 0
    while i < length:
        i = i + 1
        if num_items(Items.Carrot_Seed) < 10:
            trade(Items.Carrot_Seed)
        if can_harvest():
            harvest()
            till()
            plant(Entities.Carrots)
            move(North)
        else:
            move(North)