import logging


''' Logging configuration'''
logging.basicConfig(level=logging.INFO, filename='my_log.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')

''' Logging methods'''
logging.info('INFO message')
logging.warning('WARNING message')
logging.error('ERROR MESSAGE')
logging.critical('CRITICAL message')

''' Example of using logging'''

x = 10
y = 2

try:
    result = x / y
    logging.info(f'{y} is divided by {x}. The result is {result}')
except ZeroDivisionError as err:
    logging.warning(f'ZeroDivisionError', exc_info=True)

