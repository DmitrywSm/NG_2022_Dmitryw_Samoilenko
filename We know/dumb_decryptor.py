
alphabetLower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphabetUpper = alphabetLower.upper()
encryptText = input("enter text (eng): ")
encryptShift = int(input("enter shift of encryprion[1-25]: "))
outputText = ""

for i in encryptText: 
    positionLower = alphabetLower.find(i)
    newPositionLower = positionLower + encryptShift
    positionUpper = alphabetUpper.find(i)
    newPositionUpper = positionUpper + encryptShift
    if i in alphabetLower:
        outputText = outputText + alphabetLower[newPositionLower]
    elif i in alphabetUpper:
        outputText = outputText + alphabetUpper[newPositionUpper]
    else:
        outputText = outputText + i


print("==============================================================================") 
print("decrypted text: ")
print(outputText)
input("enter to close app")

exit()