x = input('Number: ')

y = x[::-1]

length = len(y)
sum = 0
for i in range(length):
    if i%2 == 1:
        temp = int(y[i])
        temp *= 2
        if temp > 9:
            sum = sum + (temp % 10) + temp//10
        else:
            sum = sum + temp
    else:
        temp = int(y[i])
        sum = sum + temp

if sum % 10 == 0:
    if (x[0] == '3' and x[1] == '4') or (x[0] == '3' and x[1] == '7'):
        print('AMEX\n')
    elif (x[0] == '5' and x[1] == '1') or (x[0] == '5' and x[1] == '2') or (x[0] == '5' and x[1] == '3') or (x[0] == '5' and x[1] == '4') or (x[0] == '5' and x[1] == '4'):
        print('MASTERCARD\n')
    elif x[0] == '4':
        print('VISA\n')
    else:
        print('INVALID\n')
else:
    print('INVALID\n')