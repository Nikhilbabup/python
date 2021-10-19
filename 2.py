#
# Program   : Guess The number
# Language  : Python
# Author    : Nikhil babu P
#
#
#
#
import random
print('--------------------------')
print('--- Guess that number  ---')
print('--------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100')
    guess = int(guess_text)

    if guess < the_number:
        print('Your guess of {0} too low'.format(guess))
    elif guess > the_number:
        print('Your guess of {0} too high'.format(guess))
    else:
        print('you win')

