from decimal import Decimal, ROUND_HALF_UP

def solve(value):
    return str(Decimal(value["amount"]).quantize(Decimal(value["unit"]), rounding=ROUND_HALF_UP))
