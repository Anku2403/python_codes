'Q.8 Find all prime numbers from given array.'
from math import sqrt
'Q1. Calculate the sum of all elements in an array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))

def isPrime(n):
    k = int(sqrt(int(n)))+1
    for i in range(2,k):
        if n%i==0:
            return 0
    else:
        return 1

for i in range(int(size)):
    if(isPrime(myarr[i])):
        print(f"{myarr[i]} is prime")
    else:
        print(f"{myarr[i]} is not prime")
