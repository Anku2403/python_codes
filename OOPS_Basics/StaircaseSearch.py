# StrainCase Search algorithm for 2D array whic is sorted Row & column wise.

def StaicaseSearch(mat, m, n, key):
    i = 0
    j = n-1

    while(i<m and j>=0):
        if(mat[i][j] == key):
            return (i,j)
        elif(mat[i][j] < key):
            i += 1
        else:
            j -= 1
    return -1



mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 40],
       [32, 33, 39, 50]]

m, n = 4, 4
key = int(input("Enter the number to search: "))
result = StaicaseSearch(mat, m, n, key)
if result == -1:
    print(key, "Not found")
else:
    print(result)