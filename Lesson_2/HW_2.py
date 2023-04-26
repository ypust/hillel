# Task 1

celsius = int(input('Enter the temperature in Celsius: '))


def celsius_to_fahrenheit(celsius_temperature):
    return celsius_temperature + 32 * 5 / 9


def celsius_to_kelvin(celsius_temperature):
    return celsius_temperature + 273.16


celsius_to_fahrenheit(celsius)

print('It is', celsius_to_fahrenheit(celsius), 'Fahrenheit')
print('It is', celsius_to_kelvin(celsius), 'Kelvin')

# Task 2

v1 = int(input('Set V1: '))
t1 = int(input('Set T1: '))
v2 = int(input('Set V2: '))
t2 = int(input('Set T2: '))

v_result = v1 + v2
t_result = (v1 * t1 + v2 * t2) / (v1 + v2)
print('Volume result is', v_result)
print('Temperature result is', t_result)

# Task 3

uah_usd = 38
uah_eur = 42

operation_type = int(input('''
What operation would you like to perform?
1) UAH --> USD
2) USD --> UAH
3) UAH --> EUR
4) EUR --> UAH
'''))

amount = int(input('What sum would you like to change?'))
if operation_type == 1:
    print('You will get', amount / uah_usd, 'USD')
elif operation_type == 2:
    print('You will get', amount * uah_usd, 'UAH')
elif operation_type == 3:
    print('You will get', amount / uah_eur, 'EUR')
elif operation_type == 4:
    print('You will get', amount * uah_eur, 'UAH')
else:
    print('Choose a correct operation')

# Task 4

calc_type = input('''
What calculation would you like to do?
+ (sum)
- (subtraction)
* (multiplication)
/ (division)

''')

first_number = int(input('Please, enter the first number: '))
second_number = int(input('Please, enter the second number: '))

if calc_type == '+':
    print('Result:', first_number + second_number)
elif calc_type == '-':
    print('Result:', first_number - second_number)
elif calc_type == '*':
    print('Result:', first_number * second_number)
elif calc_type == '/':
    print('Result:', first_number / second_number)
else:
    print('Choose a correct calculation')