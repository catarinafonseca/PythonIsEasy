""" Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others. """


def Equality(num1, num2, num3):
    if int(num1) == int(num2) or int(num2) == int(num3) or int(num3) == int(num1):
        return True
    else:
        return False


print(Equality(6, 5, "5"))
