#Imports
from stock import *

#define farm size
farmsize = get_world_size()

#reset everything
clear()

#global while define stocks
while True:
    keep_stock("grass", 25000, farmsize)
    keep_stock("bush", 500, farmsize)
    keep_stock("carrot", 200, farmsize)