"""Main game file"""

import random

WORDS = ['apple','banana','lemon','kiwi','orange','pineapple']
gueses_word = WORDS[random.randint(0,5)]
trying_to_guess = int(input("How many attempts do you need to guess? - "))
GUESSES = 1
words_for_show = []
while GUESSES <= trying_to_guess:
    LIST_COUNTER = 0
    user_word = input('Write word or letter: ')
    if len(words_for_show) <= 2:
        if len(user_word) > 1:
            if gueses_word == user_word:
                print(gueses_word)
                print("__ __ !!!You Win!!! __ __")
                break
            else:
                if GUESSES == trying_to_guess:
                    print("You lose!!!!")
                    break
                else:
                    print("You lose, Try again")
        if len(user_word) == 1:
            if user_word in gueses_word:
                for later in gueses_word:
                    if later == user_word:
                        words_for_show.append(user_word)
                    else:
                        words_for_show.append('*')
                print(''.join(words_for_show))
            else:
                if GUESSES == trying_to_guess:
                    print("You lose!!!!")
                    break
                else:
                    print("You lose, Try again")
    else:
        if len(user_word) > 1:
            if gueses_word == user_word:
                print(gueses_word)
                print("__ __ !!!You Win!!! __ __")
                break
            else:
                if GUESSES == trying_to_guess:
                    print("You lose!!!!")
                    break
                else:
                    print("You lose, Try again")
        if len(user_word) == 1:
            if user_word in gueses_word:
                for later in gueses_word:
                    if later == user_word:
                        words_for_show[LIST_COUNTER] = user_word
                    else:
                        LIST_COUNTER += 1
                        continue
                    LIST_COUNTER += 1
                print(''.join(words_for_show))
                if '*' not in ''.join(words_for_show):
                    print("__ __ !!!You Win!!! __ __")
                    break
            else:
                if GUESSES == trying_to_guess:
                    print("You lose!!!!")
                    break
                else:
                    print(''.join(words_for_show))
                    print("You lose, Try again")

    if GUESSES == trying_to_guess:
        print("You lose!!!!")
        break
    else:
        GUESSES += 1
