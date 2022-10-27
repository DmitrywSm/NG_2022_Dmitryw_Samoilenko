userStr = str(input("Enter your list (first, second, ...) "))
userList = userStr.split(sep=", ")
userList = list(dict.fromkeys(userList))
print(str(userList))
