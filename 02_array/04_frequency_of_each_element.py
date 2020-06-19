'Q.4 Calculate the frequency of each element in the array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)

for e in myarr:
	print(f"frequency of {e} is", end=' ')
	print(myarr.count(e))
	


