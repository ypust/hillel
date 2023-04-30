# Task 6

start_number = int(input('Enter a start number: '))
end_number = int(input('Enter an end number: '))


def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(sum_range(start_number, end_number))