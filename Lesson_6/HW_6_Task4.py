# Task 4


def change_list(list):
    if len(list) < 2:
        raise Exception('The list has less than 2 items')
    else:
        list[0], list[-1] = list[-1], list[0]
        return list
