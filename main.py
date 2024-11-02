#Imports
from stock import *

#define farm size
farmsize = get_world_size()

#reset everything
clear()

#define stocks
keep_stock("grass", 10000, farmsize)
keep_stock("bush", 2000, farmsize)
keep_stock("carrot", 1000, farmsize)
keep_stock("pumkpkin", 500, farmsize)