

from os import spawnv


numberOne = float(input("Input first number: "))
operator = str(input("Input math operator (*,/,+,-,sqrt,pow): "))
numberTwo = float(input("Input second number: "))
result = float()
spaceLine = "====================================="

print(spaceLine)

if operator == "*": 
    result = numberOne * numberTwo
elif operator == "/":
    result = numberOne / numberTwo
elif operator == "+":
    result = numberOne + numberTwo
elif operator == "-":
    result = numberOne - numberTwo
elif operator == "sqrt":
    if numberTwo != 0 :
        result = numberOne ** (1/numberTwo)
    else:result = str(float);  result = "infinity"
    print(numberOne, operator, numberTwo, "=", result )
    print(spaceLine)
    print("")
    input("Press Enter to close the program")
    exit()
elif operator == "pow":
    result = numberOne ** numberTwo
elif operator != "pow" and "sqrt" and "/" and "*" and "+" and "-":
    print("ERROR UNXEPECTED OPERATOR")
    exit() 
    
result = round(result, 3)

print(numberOne, operator, numberTwo, "=", result )
print(spaceLine)
print("")
input("Press Enter to close the program")

exit()