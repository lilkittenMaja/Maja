#Imports
from functions import *
from stock import *

size = 3
while True:
    keep_stock("grass", 20000, 3)
    keep_stock("bush", 500, 3)

#Second Carrot try
# while True:
#     trade(Items.Carrot_Seed)
#     plant(Entities.Carrots)
#     if can_harvest():
#         harvest()
#         till()
#         plant(Entities.Carrots)
#         move(North)