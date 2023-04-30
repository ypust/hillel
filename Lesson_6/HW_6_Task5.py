# Task 5

def to_dict(data):
    split_list = data.split(',')
    new_dict = dict(zip(split_list[:], split_list[:]))
    return new_dict
