# Task 1 / DiscriminantError

a_input = int(input('Enter an a:'))
b_input = int(input('Enter a b:'))
c_input = int(input('Enter a c:'))


class DiscriminantError(Exception):
    """Raised when discriminant is less than 0"""
    pass


def discriminant_calculation(a, b, c):
    discriminant_result = (b ** 2) - (4 * a * c)
    if discriminant_result < 0:
        raise DiscriminantError
    else:
        return discriminant_result


try:
    discriminant_result = discriminant_calculation(a_input, b_input, c_input)
    print('Discriminant result is', discriminant_result)

except DiscriminantError:
    print('Discriminant is less than 0')
