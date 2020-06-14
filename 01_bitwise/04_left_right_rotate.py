n=int(input("enter the number: "))
d=int(input("enter the bits to be rotated"))

"function to left rotate a number"
def leftRotate(n, d):
    a=(n<<d)
    "left shift the bit of number by d times and store it"
    b=(n>>(32-d))
    "right shift the remaining bit and store it"
    return a | b
    "add the two numbers bitwise"

"function to right rotate a number"
def rightRotate(n, d):
    a=(n>>d)
    b=(n<<(32-d))
    return a | b
print(leftRotate(n, d))
print(rightRotate(n, d))