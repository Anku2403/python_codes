'Q.2 Find largest number in the array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)
max=myarr[0]
for i in range(1,int(size)):
    if(max<myarr[i]):
        max=myarr[i]
print(f"Largest number is {max}")
