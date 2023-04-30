# Task 4


def change_list(data):
    new_list = data.split(' ')
    if len(new_list) < 2:
        return False
    else:
        new_list[0], new_list[-1] = new_list[-1], new_list[0]
        return tuple(new_list)
