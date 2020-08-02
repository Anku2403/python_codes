
N=10
x=2
while(N):
    i=2
    while(i<=x):
        if (x%i==0):
            break
        i=i+1
    if (i==x):
        print(x,end=" ")
        N=N-1
    x=x+1
