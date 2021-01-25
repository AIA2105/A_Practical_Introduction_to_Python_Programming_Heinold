from random import *

mylist = [[0] * 9 for i in range(9)]

for i in range(9):
    for j in range(9):
        x = randint(0, 9)
        while mylist[i].__contains__(x):
            x = randint(0, 9)
        while [row[j] for row in mylist].__contains__(x):
            x = randint(0, 9)
        else:
            mylist[i][j] = x


for row in mylist:
    print(row)
