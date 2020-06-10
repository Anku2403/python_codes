

def CheckNum(n):
    if(n&1==1):
        return 1
    else:
        return 0

n=int(input("Enter any number: "))
if(CheckNum(n)):
    print("Number is odd")
else:
    print("Number is even")
