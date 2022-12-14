def log (type, message):
    print("[",str(type),"] ",str(message))
def error (message):
    log("ERR", message)
    exit()
def askNumber (message):
    return int(input(message))

def divide (firstNumber,secondNumber):
    try: print("result = ", firstNumber / secondNumber)
    except ZeroDivisionError: error("dividing by 0, type another denominator") 
def multiply(firstNumber, secondNumber):
    print("result = ", firstNumber * secondNumber)
def minus(firstNumber, secondNumber):
    print("result = ", firstNumber - secondNumber)
def plus(firstNumber, secondNumber):
    print("result = ", firstNumber + secondNumber)
def root(firstNumber, secondNumber):
    if secondNumber % 2 == 0 and firstNumber < 0:
        error("out of range")
    try: print("result = ", firstNumber ** (1/secondNumber))
    except ZeroDivisionError: 
        error("infinity root")
def pow(firstNumber, secondNumber):
    print("result = ", firstNumber ** secondNumber)

def main():
    try:
        firstNumber = askNumber("Enter first number: ")
        print("(select operator)\nMinus[0]\nPlus[1]\nDivide[2]\nMultiply[3]\nRoot[4]\nPower[5]")
        operator = int(input())
        if 0 <= operator <= 5:
            secondNumber = askNumber("Enter second number: ")
            return firstNumber,secondNumber,operator
        else: error("Please enter number from [0-5]")
    except ValueError:
        error("Unexpected value. Try to enter numbers")

mainList = main()
mainOper  = mainList[2]
print("========================")

if mainOper == 0: 
    minus(mainList[0], mainList[1])
if mainOper == 1:
    plus(mainList[0], mainList[1])
if mainOper == 2:
    divide(mainList[0], mainList[1])
if mainOper == 3:
    multiply(mainList[0], mainList[1])
if mainOper == 4:
    root(mainList[0], mainList[1])
if mainOper == 5:
    pow(mainList[0], mainList[1])