length = input("enter a length in feet: ")
chooseList = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

for i in range(len(chooseList)):
    print("press", i + 1, "to convert to", chooseList[i])

choose = eval(input())
if choose - 1 < len(chooseList):
    print("You chose", chooseList[choose - 1])
else:
    print("Wrong choosing")
