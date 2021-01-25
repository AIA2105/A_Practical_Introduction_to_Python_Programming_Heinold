x = [1, 1, 2, 3, 4, 3, 0, 0]
new = []
index = 0

for i in range(len(x)):
    if not new.__contains__(x[i]):
        new.insert(index, x[i])
        index += 1

print(new)
