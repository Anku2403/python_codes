


def CountSetBits(n):
    count=0
    while(n):
        count+=n&1
        n>>=1
    return count

n=int(input("Enter any number: "))
count=CountSetBits(n)
print("Number have {} set bits".format(count))

#this can also be used.
#print(f"Number have {count} set bits)
