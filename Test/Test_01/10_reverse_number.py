def reverse(num):
    result = 0
    while(num):
        rem=num%10
        result=result*10+rem
        num = num//10
    return result
num=int(input("Enter the number:"))
n=reverse(num)
print(f"number after reversing is {n}")