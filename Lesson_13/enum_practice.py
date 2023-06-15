import enum
import requests
import logging
import random
import json

logging.basicConfig(level=logging.INFO, filename='requests.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')

""" Create a random email generator """


def email_generator():
    user_names = ["john", "liza", "nina", "alex", "emma"]
    domains = ["test.com", "mytest.com", "testmail.com", "example.com"]

    user_name = random.choice(user_names)
    domain = random.choice(domains)
    number = random.randint(1, 500)

    email = f"{user_name}{number}@{domain}"
    return email


def name_generator():
    names = ['John', 'Liza', 'Nancy', 'Nina', 'Alex', 'Mike']
    name = random.choice(names)
    return name


class StatusCode(enum.Enum):
    OK = 200
    CREATED = 201
    NOT_FOUND = 404


class EndPoints(str, enum.Enum):
    USERS = '/users'
    POSTS = '/posts'
    COMMENTS = '/comments'
    TODOS = '/todos'


class Methods(str, enum.Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


URL = 'https://gorest.co.in/public/v2'
USER_DATA = {
    "name": name_generator(),
    "email": email_generator(),
    "gender": "female",
    "status": "active"

}

POST_DATA = {
    "user_id": "2126311",
    "title": "My new post #1",
    "body": "Et bene verecundia. Et ulciscor cibus. Victus animi conturbo. "
            "Thorax capto ducimus. Ea ascisco callide. "
            "Creta deputo vergo. "
            "Aurum cogito non. Aestas denique stipes. Sopor compono appono. "
            "Arcus tondeo suppellex. Varietas abstergo corona. Summa curriculum vorax."
}

""" Add a Bearer token to the Headers """""

bearer_token = 'cc2a0e8c8bc096624186612cb01aefcfba71cfd84b1f0a7399b1b430c5120710'
headers = {
    "Authorization": "Bearer " + bearer_token
}

""" GET requests"""
get_users = requests.get(URL + EndPoints.USERS)
get_posts = requests.get(URL + EndPoints.POSTS)
get_comments = requests.get(URL + EndPoints.COMMENTS)
get_todos = requests.get(URL + EndPoints.TODOS)

""" POST requests"""
create_user = requests.post(URL + EndPoints.USERS, headers=headers, data=USER_DATA)
created_user = create_user.json()
with open('created_users.json', "a") as file:
    json.dump(created_user, file, indent=4)

create_post = requests.post(URL + EndPoints.POSTS, headers=headers, data=POST_DATA)
print(create_post.json())

""" Delete request"""

# del_user = requests.delete(URL + EndPoints.USERS + "user_id")
# print(get_users)


""" Logging GET requests"""
if get_users.status_code == StatusCode.OK.value:
    logging.info(
        f'{Methods.GET.name} request was made to "{EndPoints.USERS}". Status code is {StatusCode.OK.value}')

if get_posts.status_code == StatusCode.OK.value:
    logging.info(
        f'{Methods.GET.name} request was made to "{EndPoints.POSTS}". Status code is {StatusCode.OK.value}')

if get_comments.status_code == StatusCode.OK.value:
    logging.info(
        f'{Methods.GET.name} request was made to "{EndPoints.COMMENTS}". Status code is {StatusCode.OK.value}')

if get_todos.status_code == StatusCode.OK.value:
    logging.info(
        f'{Methods.GET.name} request was made to "{EndPoints.TODOS}". Status code is {StatusCode.OK.value}')

""" Logging POST requests"""
if create_user.status_code == StatusCode.CREATED.value:
    logging.info(
        f'{Methods.POST.name} request was made to "{EndPoints.USERS}". Status code is {StatusCode.CREATED.value}')
else:
    logging.error('Potential issue: Email can be already taken')

if create_post.status_code == StatusCode.CREATED.value:
    logging.info(
        f'{Methods.POST.name} request was made to "{EndPoints.POSTS}". Status code is {StatusCode.CREATED.value}')
else:
    logging.error('Invalid data provided')
