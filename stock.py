from functions import *

def keep_stock(item, amount, length):
    if item == "grass":
        while num_items(Items.Hay) < amount:
            plant_row_grass(length)
    elif item == "bush":
        while num_items(Items.Wood) < amount:
            plant_row_bush(length)