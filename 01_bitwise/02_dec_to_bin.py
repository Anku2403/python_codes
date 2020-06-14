n=int(input("Enter the number: "))
def decTobin(n):
    i=31
    "initializing counter with 31=sizeof(int)*8 - 1"
    while(i>=0):
        "loop will run untill counter becomes 0"
        if(1<<i)&n:
            "masking every bit of number n with 1"
            print("1", end = "")
        else:
            print("0", end = "")
        i=i-1

decTobin(n)
