treeSize = int(input("input size: "))
treeList = []
while treeSize > 0 :
    treeList.append(treeSize)
    treeSize -= 1

x = len(treeList)
for i in range(len(treeList)):
    print(str(treeList))
    del treeList[0]
input("press enter to close app")
exit()