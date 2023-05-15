import datetime


def calculate_time(check_square_function):
    def wrapper(a, b):
        begin = datetime.datetime.now()
        check_square_function(a, b)
        end = datetime.datetime.now()
        print(f"Total time taken is {end - begin} ")

    return wrapper


@calculate_time
def check_square(a, b):
    print('The square is', a * b)


check_square(2, 5)
