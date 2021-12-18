#Half diamond pattern for given N.

def diamondPattern(N):
    for i in range(N+1):
        for j in range(N-i):   #or print(" "*(N-i), end = "")
            print(" ", end = "")
        for k in range(2*i-1):  #or print("*"*(2*i-1), end = "")
            print("*", end = "")
        print()

N = int(input("Enter number:"))
diamondPattern(N)

