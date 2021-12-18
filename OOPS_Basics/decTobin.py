#Convert a number from decimal format into binary format.
def decToBin(n):

    ans = 0
    p = 1
    while n>0:
        rem = n%2
        ans = ans +rem*p
        p *=10
        n = n//2
    return ans

n = int(input("Enter decimal number:"))
print(decToBin(n))

#####################################################################
#Using BitWise operator
def decToBinBitwise(n):
    ans = 0
    p = 1
    while n>0:
        last_bit = n&1
        ans = ans +last_bit*p
        p *=10
        n = n >> 1
    return ans

print(decToBinBitwise(n))
