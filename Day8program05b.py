def checkEven(num1):
    if num1%2==0:
        return "Even"
    #return None


def checkOdd(num1):
    if num1%2==1:
        return "Odd"
    # return None

num=int(input("Enter a no:"))
print(checkEven(num))
print(checkOdd(num))
