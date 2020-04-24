import csv
import sys
from prac import finder

DbName = sys.argv[1]
SqName = sys.argv[2]
txtstr = []
name = ''
with open(DbName,'r') as file1:
    reader1 = csv.reader(file1)
    r1 = next(reader1)
    r1 = r1[1:]
    with open(SqName, 'r') as file2:
        reader2 = csv.reader(file2)
        data = next(reader2)[0]
        for str in r1:
            c = finder(data, str)
            txtstr.append(c)
        for line in reader1:
            flag = 1
            temp = line[1:]
            for i in range(len(temp)):
                if int(temp[i]) == txtstr[i]:
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                name = line[0]
if(name == ''):
    print('No Match')
else:
    print(name)

