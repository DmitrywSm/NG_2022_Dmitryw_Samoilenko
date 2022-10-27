import operator

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
}

print("a*x\u00b2+b*x+c=0")
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
scoreline = ("=====================================")
#"Des" is discriminant
Des = float((b**2)-4*a*c)
oper = str()

def rootfunc (a, b, Des, oper):
    Des = float(pow(Des, 1/2))
    x = float((operator_dict[oper] (-b, Des)) / (2 * a))
    return x

if a == 0 :
    print(scoreline)
    print("Graph is straigt line")
    print(scoreline)
    input("Press enter to close program ")
    exit()
    

if Des < 0 : 
    print("discriminant = ", Des)
    print(scoreline)
    print("Quadratic equation has no real roots")
    print(scoreline)
    input("Press enter to close program ")
    exit()
if Des == 0 : 
    x = float(rootfunc(a, b, Des, '-' ))
    print("discriminant = ", Des)
    print(scoreline)
    print("roots: x =", x )
    print(scoreline)
    input("Press enter to close program ")
    exit()

if Des > 0 :
    x1 = float(rootfunc(a, b ,Des, '-'))
    x2 = float(rootfunc(a, b ,Des, '+'))
    print("discriminant = ", Des)
    print(scoreline)
    print("roots:\n x1 = ", x1, "\n x2 = ", x2)
    print(scoreline)
    input("Press enter to close program ")
    exit()
exit()
