from array import *
'Q.7 Find if the array A is subset of array B.'
A=[]
n=input("Enter the size: ")
for i in range (int(n)):
	num1=input("Enter number: ")
	A.append(int(num1))
print(A)

B=[]
m=input("Enter the size: ")
for i in range (int(m)):
	num2=input("Enter number: ")
	B.append(int(num2))
print(B)

if(set(A).issubset(set(B))):
	print("A is subset of B")
else:
	print("A is not a subset of B")


