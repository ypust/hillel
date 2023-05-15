import datetime


def write_to_file(func):
    def time_tracker(*args):
        time_launch = datetime.datetime.now()
        result = func(*args)
        with open('function_result.txt', 'a') as file:
            file.write(f'Function launched at {time_launch} with result {result}\n')
        return result

    return time_tracker


@write_to_file
def sum_function(*args):
    return sum(args)


sum_function(2, 7)
