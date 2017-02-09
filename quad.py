print('Welcome. Input your values at the corresponding prompts.')

a = int(input('What is the value of "a?"'))
b = int(input('What is the value of "b?"'))
c = int(input('What is the value of "c?"'))
x = int(input('What is the value of "x?"'))
val = (a * x**2) + (b * x) + c

print('The following quadratic was entered %dx^2%dx+%d' %(a, b, c))
print('The value of the quadratic is %f' %val)