import random

title = 'H A N G M A N'
secret_word_list = ['python', 'java', 'kotlin', 'javascript']
select_random_from_list = random.choice(secret_word_list)
tires = 0


def guess_the_word(guess, word):
    if guess == word:
        print('You survived!')
    else:
        print('You lost!')


def replace_characters(string):
    string = string[:3] + '-' * (len(string) - 3)
    return string


def main():
    print(title)
    replace = replace_characters(select_random_from_list)
    guess_word = input(f'Guess the word {replace}: ')
    guess_the_word(guess_word, select_random_from_list)


main()
