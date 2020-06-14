num = int(input("Enter the number: "))
s = int(input("Enter the starting bit: "))
b = int(input("Enter the number of bit to set: "))

def setBit(num, s, b):
    i=s-1
    while(i<s-1+b):
        num = ((1<<i) | num)
        i=i+1
    return num

result = setBit(num, s, b)
print(result)