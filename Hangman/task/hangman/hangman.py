import random
from string import ascii_lowercase


def guess_the_word(guess, word):
    if guess == word:
        print('You guessed the word! \nYou survived!')
    else:
        print('You lost!')


def replace_characters(string):
    replace_list = list('-' * (len(string)))
    return replace_list


def find_letter_in_word(replace, secret_word):
    tries = 8
    tried = []
    while tries > 0:
        print()
        print("".join(replace))
        guess = input('Input a letter: ')
        if len(guess) != 1:
            print('You should input a single letter')
        elif guess not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        elif guess in tried:
            print("You already typed this letter")
        elif guess in secret_word:
            tried.append(guess)
            for elem in range(len(secret_word)):
                if guess == secret_word[elem]:
                    replace[elem] = guess
        else:
            tries -= 1
            tried.append(guess)
            print("No such letter in the word")
    return replace


def main():
    print('H A N G M A N')
    secret_word_list = ['python', 'java', 'kotlin', 'javascript']
    select_random_from_list = random.choice(secret_word_list)
    while True:
        game = input('Type "play" to play the game, "exit" to quit: ')
        print()
        if game == 'play':
            replace = replace_characters(select_random_from_list)
            finding = find_letter_in_word(replace, select_random_from_list)
            check = "".join(finding)
            guess_the_word(check, select_random_from_list)
        elif game == 'exit':
            break


main()
