userStr = str(input("Enter your list (1, 2, ...) "))
userList = userStr.split(sep=", ")
userList.sort(reverse= True)
sum = 0

for i in userList[1:int(len(userList)-1)]:
    sum = sum + int(i) 

print("=============================================")
print("max: ", userList[0])
print("min: ", userList[(int(len(userList))-1)])
print(f"sum({userList[1]}:{userList[int(len(userList)-2)]}) = ", sum)
print(str(userList))

input("press enter to close app")
exit()