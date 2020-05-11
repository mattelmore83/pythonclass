# High/Low game

from random import randrange

x = randrange(100) + 1
guessCount = 0

name = str((input('What is your name? ')))

print('\nHi',name,'! Let\'s play a game. Guess a number between 1 and 100.\n')

while True:
    guess = int(input('Enter a number: '))
    if guess==x:
        print('Congratulations! You got it! It took you',guessCount,'guesses!')
        break
    else:
        guessCount += 1
        if guess>=x:
            print('Lower! Try again.')
            continue
        elif guess<=x:
            print('Higher! Try again.')
            continue
