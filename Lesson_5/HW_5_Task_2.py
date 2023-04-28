# Task 2 Interactive calculator

user_input = input('Enter the numbers and operation sign:')
user_input_data = user_input.split(' ')


class FormulaError(Exception):
    """User input data is less than 3"""
    pass


def calculator(user_numbers):
    try:
        if len(user_numbers) == 3:
            if user_numbers[1] == '+':
                return float(user_numbers[0]) + float(user_numbers[2])
            if user_numbers[1] == '-':
                return float(user_numbers[0]) - float(user_numbers[2])
            else:
                raise FormulaError('Invalid operation type')
        else:
            raise FormulaError('Input data is less than 3')
    except ValueError:
        raise FormulaError('Invalid input')


try:
    print(calculator(user_input_data))
except FormulaError as error:
    print('FormulaError Exception', error)