def is_prime (x):
    ''' (int) -> boolean

    Returns true if a given int value is a prime number.

    >>> is_prime (17)
    True
    >>> is_prime (25)
    False
    >>> is_prime (14057)
    True
    '''
    if x <= 1:
        return False
    if x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

for i in list(range(2, 100)):
    if is_prime(i):
        print('%s is Prime!' %i)
