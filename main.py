#Imports
from stock import *

#reset everything
clear()

#define variables
farmsize = get_world_size()

#define stocks
keep_stock("grass", 10000, farmsize)
keep_stock("bush", 2000, farmsize)
keep_stock("carrot", 1000, farmsize)
keep_stock("pumpkin", 500, farmsize)

#-------------------------------------------------
#TO DO
#-------------------------------------------------

#Redo whole planting and tilling stuff for carrots

#separate Harvesting from planting for pumpkins
#To replant died pumpkins