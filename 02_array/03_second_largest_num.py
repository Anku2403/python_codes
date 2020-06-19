'Q3. Find second larget number in the array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
largest=max(myarr[0], myarr[1])
sec_largest=min(myarr[0], myarr[1])
for i in range(2, int(size)):
	if(largest<myarr[i]):
		sec_largest=largest
		largest=myarr[i]
	elif(sec_largest<myarr[i] and largest!=myarr[i]):
		sec_largest=myarr[i]

print(f"The largest element is: {largest}" )
print(f"The second largest element is: {sec_largest}")
