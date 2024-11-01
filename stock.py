from planting import *

def keep_stock(item, amount, size):
    if item == "grass":
        while num_items(Items.Hay) < amount:
            i = 0
            while i < size:
                i = i + 1
                plant_row_grass(size)
                move(East)
    elif item == "bush":
        while num_items(Items.Wood) < amount:
            i = 0
            while i < size:
                i = i + 1
                plant_row_bush(size)
                move(East)
    elif item == "carrot":
        while num_items(Items.Carrot) < amount:
            i = 0
            while i < size:
                i = i + 1
                plant_row_carrot(size)
                move(East)