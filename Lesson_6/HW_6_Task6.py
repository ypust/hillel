# Task 6

def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))
