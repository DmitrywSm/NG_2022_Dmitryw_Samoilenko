
def askString ():
    userString = input("Enter your text: ")
    return userString

optionList = ["Sort text", "Count number of elements", "Output only vowels", "Output only consonants", "Break by words and print words from the end", "Print word by number", "Enter the line again", "Exit"]

def sortText (userString):
    userString = list(userString)
    sortedList = sorted(userString, reverse=False)
    print(''.join(sortedList))

def countNumber(userString):
    print(len(userString))

def onlyVowels(userString):
    vowelsSet = {'a', 'i', 'e', 'o', 'u', 'y'}
    for letter in userString.lower():
        if letter in vowelsSet:
            print(letter, end="")
    print('')
def onlyConsonants (userString):
    consonantsSet = { 'b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y'} 
    for letter in userString.lower():
        if letter in consonantsSet:
            print(letter, end="")
    print('')

def breakAndPrint (userString):
    wordList = breakByWord(userString)
    print(sorted(wordList, reverse = True))

def breakByWord (userString):
    return userString.split(sep =" ")

def wordByNumber (userString):
    wordList = breakByWord(userString)
    try: 
        userIndex = int(input("Enter index of word: "))
        print(wordList[userIndex])
    except: print("unexpected index")

def writeLine (userString):
    print(userString)

def exitFunc(userString): 
    return 1

functionDict = {
    "0": sortText,
    "1": countNumber,
    "2": onlyVowels,
    "3": onlyConsonants,
    "4": breakAndPrint,
    "5": wordByNumber,
    "6": writeLine,
    "7": exitFunc,
}

def showOptions (optionList):
    for element in optionList :
        print( "[",str(optionList.index(element)),"] " ,element)

def askOption ():
        userChoise = input("choose the option ")
        return userChoise
     
def main (optionList):
    userString = askString()
    i = 0 
    while i != 1 :
        showOptions(optionList)
        try: 
            callfunc = functionDict[askOption()]
            print("===========================")
            a = callfunc(userString)
            print("===========================")
        except: 
            print("===========================")
            print("type another option index")
            print("===========================")
        if a == exitFunc(userString):
            print("bye")
            exit()

main(optionList)
