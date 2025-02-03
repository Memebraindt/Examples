length = int(input('Enter number of rows: '))
l2 = length * 2
for i in range(l2 - 1):
    for j in range(l2):
        if ((i < j) and (l2-i-2 < j)) or \
            (j <= i)and (l2-j-1 > i):
            print('*', end='')
        else:
            print(' ', end='')
    print()
