while True:

    fahr_temp = int(input('Hullo, I\'m Tempe, the temperature converter.  Please input the temperature in Fahrenheit that you would like to have converted to Centigrade: '))
    print('You inputted %sF, that is %dC!' %(fahr_temp, (fahr_temp - 32) / (9/5)))
    dump = input('Would you like to exit?')
    if dump.lower() == 'yes':
        break



