array = [[1,2],[3,4]]

def diagonal_sum(array):
    result = 0
    n = len(array)
    for i in range(n):
       	result += array[n-i-1][n-i-1]
    print(result)
 
diagonal_sum(array)  

