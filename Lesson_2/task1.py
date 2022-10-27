phraseList = str(input("Enter your phrase:"))
phraseList = phraseList.lower()
phraseCount = {}

#makes new key for every unique element and gives values from number of every unique element
for i in  phraseList: 
    phraseCount [i] = phraseList.count(i)    

#sorts keys by values 
sortedCount = sorted(phraseCount, key=phraseCount.get, reverse = True)

#for every key prints key+value from sorted dictionary
for perKey in sortedCount:
    print(str(perKey), ": ", str(phraseCount.get(perKey)))
