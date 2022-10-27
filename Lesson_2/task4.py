factSize = int(input("input number to get factorial: "))
userFactSize = factSize
factList = []
multip = 1

while factSize > 0 :
    factList.append(factSize)
    factSize = factSize - 1 

for i in factList:
    print(multip, "* ", i)
    multip = multip * i
print("====================================")
print( userFactSize,"!" ," = ",multip)


