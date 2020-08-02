x=int(input("Enter the number:"))
a=x&(x-1)
if(a==0):
        print(f"{x} is a power of 2.")
else:
        print(f"{x} is not a power of 2.")