def closest(num, list):
    myList = sorted(list)
    for i in range(len(myList)):
        if myList[i] >= num:
            return myList[i - 1]


print(closest(8, [1, 6, 3, 9, 11]))
