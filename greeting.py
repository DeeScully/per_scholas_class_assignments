def greet():
    name = input('What is your name?')
    print('Nice to meet you, %s' %(name))

    fave_color = input('%s, what is your favorite color?' %(name))
    print('%s?  That\'s a nice color, %s!' %(fave_color, name))

    fave_food = input('%s, what is your favorite food?' %(name))
    print('%s sounds yummy, %s' %(fave_food, name))

    end_game = input('%s, do you have to go?' %name)
    if end_game == 'no':
        greet()

greet()