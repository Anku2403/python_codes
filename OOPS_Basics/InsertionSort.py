def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        j=i
        while (arr[j-1] > arr[j] and j > 0):
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j-=1
            

array = [10,5,67,4,2,1]
InsertionSort(array)
print(array)