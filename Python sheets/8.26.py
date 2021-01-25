def right(x):
    count = 0
    arr = []
    for i in x:
        if i == ")":
            arr.insert(count, count)
            count += 1

    index = 0
    for i in range(int(x[-4]) + 1):
        for j in range(int(x[-2]) + 1):
            print(arr[index], end=" ")
            index += 1
        print("")


def left(y):
    new= y.split("  ")
    for i in range(len(new)):
        for j in range(len(new[0].split(" "))):
            print("(",i,",",j,")",end=" ")
        print("")

x = input()
right(x)
y = input()
left(y)
