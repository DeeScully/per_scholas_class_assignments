tally = 0
num_of_nums = int(input('Please type how many numbers you would like to average: '))
#num_list = list()

for i in range(1, num_of_nums + 1):
    inp = input('Please type the number ' + str(i) + ' numeral: ')
    input_num = int(inp)
    #num_list.append(input_num)
    tally += input_num
    print('You typed %d, and it has been added to your average calculation.' %input_num)

average = tally / num_of_nums

print('You inputted %d numbers and the average is %f' %(num_of_nums, average))