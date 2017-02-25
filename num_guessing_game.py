import random as rand
max_num = 10
secret_num = 0
guesses_left = 0
game_over = False

def new_game():
    global secret_num, guesses_left

    secret_num = rand.randint(1, max_num)
    guesses_left = 3
    print('Let\'s play a game.  You have three guesses to guess my secret number.  It will be between 1-10.')
    return secret_num

def input_guess():
    global guesses_left, game_over

    invalid = True
    while invalid:
        try:
            guess_str = input('What is your guess?')
            guess_int = int(guess_str)

        except:
            print('You did not input an integer.  Please try again.')
            continue

        if guess_int < 1 or guess_int > 10:
            print('Your number is outside the valid range.  Please try again.')
            continue

        invalid = False

    print('Your guess was: %d' %(guess_int))

    if guess_int == secret_num:
        print('That\'s right.  You WIN!')
        game_over = True
    elif (abs(guess_int - secret_num) == 1) and guesses_left > 1:
        print('You\'re HOOOOOT.')
        guesses_left -= 1
    elif (abs(guess_int - secret_num) == 2) and guesses_left > 1:
        print('You\'re Warm.')
        guesses_left -= 1
    elif guesses_left > 1:
        print('You\'re Coooooold.')
        guesses_left -= 1
    else:
        print('Ohhh that\'s wrong.  The secret number was %d.' %(secret_num))
        game_over = True

new_game()
while not game_over:
    input_guess()



