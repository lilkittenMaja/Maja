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
keep_stock("pumpkin", 500, farmsize)

#-------------------------------------------------
#TO DO
#-------------------------------------------------

#Put tilling into it's own function
#Till the whole field for plants that need it
#Track if field is tilled or not

#separate Harvesting from planting for pumpkins
#To replant died pumpkins