# Task 4

entered_data = input('Enter your numbers:')
splited_data = entered_data.split(' ')
print(splited_data)


def change_list(numbers):
    new_list = list(numbers)
    if len(new_list) < 2:
        return False
    else:
        new_list[0], new_list[-1] = new_list[-1], new_list[0]
        return tuple(new_list)


print(change_list(splited_data))
