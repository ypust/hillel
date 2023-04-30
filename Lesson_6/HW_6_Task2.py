# Task 2

entered_square_side = int(input('Enter a square side:'))


def square(square_side):
    perimeter = square_side * 4
    area = square_side * square_side
    diagonal = square_side * (2 ** 0.5)
    return perimeter, area, diagonal


perimeter, area, diagonal = square(entered_square_side)
print("Perimeter:", perimeter)
print("Area:", area)
print("Diagonal:", diagonal)
