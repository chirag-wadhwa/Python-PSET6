while True:
    x = input('Height: ')
    if not x.isdigit():
        continue
    else:
        if int(x) > 0 and int(x) < 9:
            break
        else:
            continue

y = int(x)

for i in range(y):
    for j in range((2 * y) + 2):
        if (j>=(y-i-1) and j<y) or ((j<((2 * y) +2)-(y-i) + 1) and j>=y+2 ):
            print('#',end = '')
        else:
            print(' ', end='')
    print('\n')