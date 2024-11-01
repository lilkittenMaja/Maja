from functions import *

def keep_stock(item, amount, length, width):
    if item == "grass":
        while num_items(Items.Hay) < amount:
            i = 0
            while i < width:
                i = i + 1
                plant_row_grass(length)
                move(East)
    elif item == "bush":
        while num_items(Items.Wood) < amount:
            i = 0
            while i < width:
                i = i + 1
                plant_row_bush(length)
                move(East)
    elif item == "carrot":
        while num_items(Items.Carrot) < amount:
            plant_row_carrot(length)