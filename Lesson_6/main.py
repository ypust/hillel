from Lesson_6.HW_6_Task1 import check_number_division
from Lesson_6.HW_6_Task2 import square
from Lesson_6.HW_6_Task3 import is_prime
from Lesson_6.HW_6_Task4 import change_list
from Lesson_6.HW_6_Task5 import to_dict
from Lesson_6.HW_6_Task6 import sum_range


if __name__ == '__main__':
    # Task 1

    check_number_division(8)

    # Task 2
    perimeter, area, diagonal = square(14)
    print("Perimeter:", perimeter)
    print("Area:", area)
    print("Diagonal:", diagonal)

    # Task 3
    print(is_prime(6))

    # Task 4
    print(change_list(['hello', 'nice', 'to', 'meet', 'you']))

    # Task 5
    print(to_dict(['Hello', 'nice', 'fine']))

    # Task 6
    print(sum_range(13, 8))

