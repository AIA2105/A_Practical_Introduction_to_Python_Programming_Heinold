from random import randint

x=[]
zeroCount=0
max=0

for i in range(100):
    x.insert(i,randint(0,1))
    if x[i]==0:
        zeroCount=zeroCount+1
        if zeroCount>max:
            max=zeroCount
    else:
        zeroCount=0
print(x)
print('the largest number of zeros in a row= ',max)