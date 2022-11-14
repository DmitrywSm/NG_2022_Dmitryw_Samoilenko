userStr = (input("Enter your list (1, 2, ...) "))
userList = userStr.split(sep=", ")
sum = 0

for element in range(0, len(userList)):
    userList[element]= int(userList[element])

sortedList = sorted(userList, reverse= True)

for element in sortedList[1:int(len(sortedList)-1)]:
    sum = sum + int(element) 

print("=============================================")
print("max: ", sortedList[0])
print("min: ", sortedList[(int(len(sortedList))-1)])
print(f"sum({sortedList[1]}:{sortedList[int(len(sortedList)-2)]}) = ", sum)