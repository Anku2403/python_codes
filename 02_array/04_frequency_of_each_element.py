'Q.4 Calculate the frequency of each element in the array.'
myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)
def frequency(arr):
	for i in range(int(size)):
		count=0
		for e in arr:
			if e==arr[i]:
				count+=1
		print(f'Frequency of {arr[i]} is {count}')

frequency(myarr)


