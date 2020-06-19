'Q1. Calculate the sum of all elements in an array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)
#print(f"The sum of array is {sum(myarr)}")
print("sum: %d" %sum(myarr))
