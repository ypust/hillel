car = {
    'Brand': "Opel",
    'Year': 2021,
    'Seats number': 4,
    'Is avaliable': True
}

# Нужно объединить списки
print(list(car.values()))

car = {
    'Brand': "Opel",
    'Year': 2021,
    'Seats number': 4,
    'Is avaliable': True
}

# создать уникальный список без повторений данных. нужно преобразовать его в список и работать дальше со списком
my_list = [1, 3, 4, 21, 21, 4, 1, 42]
print(list(set(my_list)))

# list comprehension is used for making a list easier to create and work with. Тернарый оператор
new_list = [x**2 for x in range(8)]
print(new_list)