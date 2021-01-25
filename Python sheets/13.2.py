def add_excitement(list):
    for i in range(len(list)):
        list[i] = list[i] + '!'


def add_excitement2(list):
    list2 = list
    for i in range(len(list)):
        list2[i] = list[i] + '!'
    return list2


x = ['ad', 'bg', 'hc', 'dj', 'ek']
print(x)

# add_excitement(x)
# print(x)

print(add_excitement2(x))
