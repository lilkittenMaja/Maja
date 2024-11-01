#Imports
from functions import *
from stock import *

#define farm size
farml = 3
farmw = 3

#reset everything
clear()

#global while define stocks
while True:
    keep_stock("grass", 25000, farml, farmw)
    keep_stock("bush", 500, farml, farmw)
    keep_stock("carrot", 200, farml, farmw)