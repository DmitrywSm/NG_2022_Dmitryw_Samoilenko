factSize = int(input("input number to get factorial: "))
userFactSize = factSize
factList = {1}
multip = 1

while factSize > 0 :
    factList.add(factSize)
    factSize = factSize - 1 
    

for x in factList:
    print(multip, " * ", x )
    multip = multip * x
print("====================================")
print( userFactSize,"!" ," = ",multip)