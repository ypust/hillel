# Task 1 / Capitalize the items in the list

lower_names = ["john", "marta", "james", "amanda", "marianna"]
new_upper_names = []
for name in lower_names:
    new_upper_names.append(name.capitalize())
print(new_upper_names)

# Task 2 / Align names to the right

friends_list = ['John', 'Marta', 'James', 'Amanda', 'Marianna']
title = 'NAME'
print(title.center(30, '*'))
for friends in friends_list:
    print(f'{friends : >30}')

# Task 3 /

CamelCase = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for word in CamelCase:
    snake_case = ""
    for letter_position in range(len(word)):
        if letter_position == 0:
            snake_case += word[0].lower()
        elif word[letter_position].isupper():
            snake_case += "_" + word[letter_position].lower()
        else:
            snake_case += word[letter_position]
    snake_case_list.append(snake_case)
print(snake_case_list)

# Task 4 / Invention of the programming languages

programmers_dict = {
    'Python': 'Guido van Rossum ',
    'Java': 'Green Team',
     'C#': 'Microsoft Corporation',
     'PHP': 'Rasmus Lerdorf'
                    }

for key, value in programmers_dict.items():
    print(f'My favorite programming language is {key}. It was created by {value}')

programmers_dict.popitem()
print(programmers_dict)

# Task 5 / English - German dictionary

e2g = {
    'stork': 'storch',
    'hawk': 'falke',
    'woodpecker': 'specht',
    'owl': 'eule'
}
print(e2g)

# Print a German variant of 'Owl'
print(e2g.get('owl'))

# Add two more words to the dictionary
e2g['sun'] = 'sonne'
e2g['moon'] = 'mond'
print(e2g)

# Print a key-value of the dictionary in a list view
print(e2g.values())
print(e2g.keys())

# Task 5 / Create a dictionary with the subjects

subjects = {
    'science': {
        'physics': ['nuclear physics', 'optics', 'thermodynamics'],
        'computer science': [],
        'biology': []
    },

    'humanities': {

    },
    'public': {

    }
}
print(subjects['science'].keys())
print(subjects['science']['physics'])

# Task 6 /

numbers_dict = {}

for number in range(1, 16):
    numbers_dict[number] = number ** 2

print(numbers_dict)
