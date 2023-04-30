# Task 1
import math
entered_number = int(input('Enter a number:'))

def check_number_division(n):
    if n > 0 and math.log2(n).is_integer():
        print('YES')
    else:
        print('NO')


check_number_division(entered_number)
