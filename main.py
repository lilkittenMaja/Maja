#Imports
from functions import *
from stock import *

keep_stock(20000, Entities.Bush)

clear()
while True:
    if can_harvest():
        harvest_and_move(North)
    elif can_harvest() == False:
        plant(Entities.Bush)

#Second Carrot try
# while True:
#     trade(Items.Carrot_Seed)
#     plant(Entities.Carrots)
#     if can_harvest():
#         harvest()
#         till()
#         plant(Entities.Carrots)
#         move(North)