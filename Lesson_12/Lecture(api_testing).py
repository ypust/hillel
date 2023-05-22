from pprint import pprint
import requests

#  get the request result and transform it into json format
# pprint(get_result.json())

URL = 'https://reqres.in/'

''' Get request'''
get_result = requests.get(URL + 'api/users?page=2')


''' POST request'''

DATA = {
    'name': 'Liza',
    'job': 'leader'
}

post_result = requests.post(URL + 'api/users', data=DATA)
print(post_result.json())
pprint(get_result.json())

