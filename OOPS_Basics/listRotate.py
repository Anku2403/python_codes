lst = [3,5,2,7,8,9]
step = 4
print(lst)
n = len(lst)
for a in range(step):
    key = lst[-1]

    for i in range(n-1, 0, -1):
        lst[i] = lst[i-1]
    
    lst[0] = key
print(lst)
