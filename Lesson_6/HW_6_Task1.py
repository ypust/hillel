# Task 1
import math


def check_number_division(n):
    if n > 0 and math.log2(n).is_integer():
        print('YES')
    else:
        print('NO')
