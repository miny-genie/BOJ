# -------------------- Case 1: Python3 AC --------------------
# ---------- Import ----------
import decimal
from decimal import Decimal as D
import sys
input = sys.stdin.readline

# ---------- Function ----------
def changeDecimalObject(*args):
    Decimal_Object = []
    for val in args:
        Decimal_Object.append(D(val))
    return Decimal_Object

# ---------- Main ----------
decimal.getcontext().prec = 1000

molA, molB = map(int, input().split())
sizeA, sizeB, ml = map(int, input().split())

# Initialization
how_many_drink = 0 
drink_percent = 0

# Using 'Decimal' object
molA, molB, sizeA, sizeB, ml, drink_percent =\
    changeDecimalObject(molA, molB, sizeA, sizeB, ml, drink_percent)

# First end condition
if molA == molB == 0:
    print("gg")
    exit()
    
while True:
    # Second end condition
    if drink_percent > molA:
        break
    
    # Third end condition
    if sizeA < ml:
        break
    
    drink_percent = molA
    how_many_drink += 1
    
    # Fourth end condition
    if sizeB < ml:
        break
    
    molA = ((molA * sizeA) + (molB * ml) - (molA * ml)) / sizeA
    molB = ((molB * sizeB) - (molB * ml)) / sizeB

# how_many_drink is inbound
if 0 < how_many_drink < 51:
    print(format(how_many_drink, 'X'))

# how_many_drink is outbound
else:
    print("gg")
    
    
# -------------------- Case 2: Python3 AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
molA, molB = map(int, input().split())
sizeA, sizeB, ml = map(int, input().split())

# Initialization
how_many_drink = 0 
drink_percent = 0

# First end condition
if molA == molB == 0:
    print("gg")
    exit()
    
while True:
    # Second end condition
    if drink_percent > molA:
        break
    
    # Third end condition
    if sizeA < ml:
        break
    
    drink_percent = molA
    how_many_drink += 1
    
    # Fourth end condition
    if sizeB < ml:
        break
    
    molA = ((molA * sizeA) + (molB * ml) - (molA * ml)) / sizeA
    molB = ((molB * sizeB) - (molB * ml)) / sizeB

# how_many_drink is inbound
if 0 < how_many_drink < 51:
    print(format(how_many_drink, 'X'))

# how_many_drink is outbound
else:
    print("gg")