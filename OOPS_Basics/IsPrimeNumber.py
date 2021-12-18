#To check a number is prime or not

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = int(input("Enter thr number:"))

if(isPrime(n)):
    print("Yes, It is prime.")
else:
    print("Not a prime.")

#Print all prime number in given range.

for i in range(1, n+1):
    if(isPrime(i)):
        print(i, end = ",")