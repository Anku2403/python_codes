
N=10
x=2
while(N):
    global i
    for i in range(2, x):
        if (x%i==0):
            break
    if (i==x):
        print(x,end=" ")
        N=N-1
    x=x+1
