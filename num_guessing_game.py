import random

my_num = random.random() * 10
guess_num = 3
game_over = False

def wrong_guess():
    global guess_num
    guess_num -= 1

def valid_num():
    valid_input = False

    while not valid_input:
        try:
            guess = int(input('What is your guess?  Please type an integer from 1 to 10.'))
            valid_input = True
        except:
            print('You did not input a valid integer.  Please try again.')

print('Let\'s play a game.  I have a number from 1 to 10.  You try to guess what it is!')

while not game_over and guess_num > 0:
    if valid_num() == my_num:
        print('That\'s right.  You WIN!')
        game_over = True
    elif valid_num() == my_num + 1 or valid_num() == my_num - 1:
        print('You\'re HOOOOOT.')
        wrong_guess()
    elif valid_num() == my_num + 2 or valid_num() == my_num - 2:
        print('You\'re warm.')
        wrong_guess()
    else:
        print('You\'re cold.')
        wrong_guess()







