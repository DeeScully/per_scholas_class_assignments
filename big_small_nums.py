def is_biggest(num_list):
    hi = 0

    for i in num_list:
        if i > hi:
            hi = i

    return hi

def is_smallest(num_list):
    lo = is_biggest(num_list)

    for i in num_list:
        if i < lo:
            lo = i

    return lo

numbers = list()
num_collected_done = False

while num_collected_done == False:
    try:
        num_str = input('Please input an integer; or, if done inputting, type "c."')
        if num_str.lower() == 'c':
            num_collected_done = True
            continue
        num = int(num_str)
        numbers.append(num)
    except ValueError:
        print('You did not input an integer.  Please try again.')

print('%d is the largest number in your set' %(is_biggest(numbers)))
print('%d is the smallest number in your set' %(is_smallest(numbers)))


