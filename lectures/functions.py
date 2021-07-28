# Basic structure of a function
""" 
def FuntionName(input):
    Action
    return Output 
"""


def addOne(Number):
    Number = Number + 1
    return Number


Var = 0
print(Var)
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(2.1)
# this one is gonna add the 2 float numbers and then the addOne function
Var5 = addOne(2.1 + 3.4)
print(Var2)
print(Var3)
print(Var4)
print(Var5)


def addOneAddTwo(Number1, Number2):
    Output = Number1 + 1
    Output += Number2 + 2
    return Output

Sum = addOneAddTwo(1,2)
print(Sum)

