'Q.11 Check if array contains unique elements.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)

""" 
def checkUnique(myarr, n):
    for i in range(n):
       for j in range(i+1, n):
            if(myarr[i]==myarr[j]):
                return 0
    return 1 
"""
if(len(myarr)==len(set(myarr))):
    print("Yes, Array contain unique element")
else:
    print("No, Array does not contain unique element")
