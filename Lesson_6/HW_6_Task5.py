# Task 5
list_data = input('Enter your data:')
split_list = list_data.split(',')
print(split_list)


def to_dict(lst):
    new_dict = dict(zip(lst[:], lst[:]))
    return new_dict


print(to_dict(split_list))