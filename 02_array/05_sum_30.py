'Q.5 Count the number of pairs in the array whose sum are equal to 30.'

myarr=[]
size=input("Enter the size: ")
for i in range (int(size)):
	num=input("Enter number: ")
	myarr.append(int(num))
print(myarr)
n=int(size)

def countPair(A, n):
    count=0
    for i in range(n):
        for j in range(i+1, n):
            if(A[i]+A[j]==30):
                count+=1
    return count

number = countPair(myarr, n)
print(f"total number of pair whose sum is 30 is {number}")


