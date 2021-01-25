
def mymax(numOfPrimes):

    if numOfPrimes <=25:
        return 100
    elif numOfPrimes <=168:
        return 1000
    elif numOfPrimes <=1229:
        return 10000
    elif numOfPrimes <=9592:
        return 100000
    elif numOfPrimes <=78498:
        return 1000000
def primeBetween(lower,upper):
    list=[]
    for num in range(lower, upper):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list.append(num)
    return list
def primes(n=100):
        mylist= primeBetween(1, mymax(n))
        for i in range(n):
            print(i+1,'->',mylist[i])

def primes2(n=100,start=2):
    mylist= primeBetween(start, mymax(n))
    for i in range(n):
        print(i+1,'->',mylist[i])


primes(100)
print('--------------------')
primes2(100,7)