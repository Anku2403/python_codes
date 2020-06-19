'Q.9 Reverse the element of array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)
myarr.reverse()
print("After reversing array")
print(myarr)