#!/usr/bin/python3
def magic_calculation(a, b):
    c = 0
    if a < b:
        from magic_calculation_102 import add
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
    else:
        from magic_calculation_102 import sub
        return sub(a, b)
    return c

