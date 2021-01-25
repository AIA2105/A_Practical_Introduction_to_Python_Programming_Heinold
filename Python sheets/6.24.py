
num = input("Enter the number: ")
new = num.split("^", 2)
newPower = int(new[1]) - 1
print(new[1]+new[0]+"^"+str(newPower))
