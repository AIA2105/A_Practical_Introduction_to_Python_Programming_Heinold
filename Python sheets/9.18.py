from random import randint


mylist=[[0]*6 for i in range(6)]

arr = [[randint(0,6),randint(0,6)]]
while len(arr) < 12:
    x= randint(0,5)
    y= randint(0,5)
    small = [x,y]
    if not arr.__contains__(small):
        arr.append(small)

for i in range(12):
    mylist[arr[i][0]][arr[i][1]]=1

for row in mylist:
    print(row)

