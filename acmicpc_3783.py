# Before 1384 / 1400
# After  1391 / 1400 (+7)

# ---------- Import ----------
import decimal
decimal.getcontext().prec = 153

# ---------- Function ----------
def cube_root(input_num):
    decimal_num = decimal.Decimal(input_num)
    pow_num = decimal.Decimal('1') / decimal.Decimal('3')
    
    decimal_num = decimal.Decimal(decimal_num ** pow_num)
    decimal_num = round(decimal_num, 101)
    
    decimal_num = decimal.Decimal(decimal_num)\
        .quantize(
            decimal.Decimal('.0000000000'),
            rounding=decimal.ROUND_DOWN
        )
    
    return decimal_num

# ---------- Main ----------
for _ in range(int(input())):
    input_num = input().rstrip()
    print(cube_root(input_num))
    
# ---------- Comment ----------
# L06: remove "+ '.0000000000'"
# L13: change "'.0000000001'" > "'.0000000000'"
# L02: change 1000 > 153
# L10: change 500 > 101

# L10: 101 is ok, 100 is not ok
# L02: 153 is ok, 152 is not ok

# L06: https://docs.python.org/ko/3/library/decimal.html#decimal.Context
# L10: https://docs.python.org/ko/3/library/decimal.html#decimal.Decimal
# L17: https://docs.python.org/ko/3/library/decimal.html#decimal.Decimal.quantize

# Context(
    # prec=28,
    # rounding=ROUND_HALF_EVEN,
    # Emin=-999999999,
    # Emax=999999999,
    # capitals=1,
    # flags=[],
    # traps=[Overflow, InvalidOperation, DivisionByZero]
#)