x = input('Text: ')

letters = 0
sentences = 0
words = 1
for i in range(len(x)):
    if x[i] == ' ':
        words += 1
    elif (x[i] == '.' or x[i] == '?' or x[i] == '!' ):
        sentences += 1
    elif x[i].isalpha() :
        letters += 1

L = letters / words * 100
S = sentences / words * 100
temp = 0.0588 * L - 0.296 * S - 15.8
grade = round(temp)

if grade < 1:
    print('Before Grade 1')
elif grade > 16:
    print('Grade 16+')
else:
    print('Grade',grade)
