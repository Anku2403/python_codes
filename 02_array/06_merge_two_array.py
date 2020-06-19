'Q.6 Merge two arrays. Given arrays A and B merge it to new array C and print C.'
myarr1=[]
n=input("Enter the size: ")
for i in range (int(n)):
	num=input("Enter number: ")
	myarr1.append(int(num))
print(myarr1)

myarr2=[]
m=input("Enter the size: ")
for i in range (int(m)):
	num=input("Enter number: ")
	myarr2.append(int(num))

myarr3=myarr1+myarr2
print("After merging above two array: ")
print(myarr3)