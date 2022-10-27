treeSize = int(input("input size: "))
userTreeSize = treeSize
strNumber = 0

def Writer (treeSize, strNumber):
    treeSize -= strNumber
    while treeSize > 0:
        print(treeSize, end=" ")
        if treeSize == 1:
            strNumber += 1
            print("\n", end="")
            return strNumber
        treeSize -= 1

while strNumber != userTreeSize:
   strNumber = Writer(treeSize, strNumber)
