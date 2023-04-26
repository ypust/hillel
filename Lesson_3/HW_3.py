# Task 1

user_word = str(input('Enter your word: '))


def check_palindrome(word):
    return word == word[::-1]


if check_palindrome(user_word):
    print('+')
else:
    print('-')


# Task 2

user_entered_text = input('Enter your text: ').lower()
word_to_find = input('What word would you like to find? : ').lower()

if user_entered_text.__contains__(word_to_find):  # also 'in' can be used
    print('Yes')
else:
    print('No')

# Task 3
entered_word = input('Enter the word: ')
beginning_replacement = "www"
end_replacement = 'zzz'

if entered_word[0:3] == 'abc':
    result = entered_word.replace(entered_word[0:3], beginning_replacement, 1)
    print(result)
else:
    result = entered_word + end_replacement
    print(result)


# Task 4
email_address = input('Please, enter your email: ')
if email_address.__contains__('@') and email_address.__contains__('.'):
    print('Yes')
else:
    print('No')

# Task 5

text_placeholder = input('Enter your text: ')
split_text = text_placeholder.split(' ')
if len(split_text) >= 3:
    print(split_text[-3:])
else:
    print('Your text has', len(split_text), 'words.', 'The number of words is less than 3')
