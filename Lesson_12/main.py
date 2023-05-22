import argparse

parser = argparse.ArgumentParser(description='Discriminant calculations')

parser.add_argument('--a', type=int, default=0, help='a parameter. By default a = 0')
parser.add_argument('--b', type=int, help='b parameter')
parser.add_argument('--c', type=int, help='c parameter')

args = parser.parse_args()


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
    discriminant_result = discriminant_calculation(args.a, args.b, args.c)
    print('Discriminant result is', discriminant_result)

except DiscriminantError:
    print('Discriminant is less than 0')
