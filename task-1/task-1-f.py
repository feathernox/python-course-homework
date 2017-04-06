# BazQux.

numbers = range(1, 101)

for i in numbers:
    print(i, end=' ')
else:
    print('')

for i in numbers:
    if i % 15 == 0:
        print('BazQux', end=' ')
    elif i % 5 == 0:
        print('Qux', end=' ')
    elif i % 3 == 0:
        print('Baz', end=' ')
    else:
        print(i, end=' ')
else:
    print('')
