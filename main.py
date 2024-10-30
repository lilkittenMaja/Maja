#Simple plant loop
# while True:
#     if can_harvest():
#         harvest()
#         move(North)

#Bush plant
# while True:
#     if can_harvest():
#         harvest()
#         plant(Entities.Bush)
#         move(North)

#Second Carrot try
while True:
    if can_harvest():
        harvest()
        till()
        #trade(Items.Carrot_Seed)
        plant(Entities.Carrots)
        move(North)