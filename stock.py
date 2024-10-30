from functions import *

def keep_stock(amount, item):
    if num_items(item) < amount:
        plant_field(item)
    