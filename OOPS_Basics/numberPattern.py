"""
Print the following pattern for a give N.
N=3

1
2 3
4 5 6
"""
def patternNumber(N):
    val = 1
    for i in range(N+1):
        for j in range(i):
            print(val, end=" ")
            val += 1
        print()

N = int(input("Enter number:"))
patternNumber(N)