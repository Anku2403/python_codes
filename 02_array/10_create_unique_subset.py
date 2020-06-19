'Q.10 Create subset from the array. (extract unique element from the array)'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)
n=int(size)

subset=[]
for e in myarr:
    if not e in subset:
        subset.append(e)

print(subset)
