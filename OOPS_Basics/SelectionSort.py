#Repeatedly find the minimum element from unsorted part and putting it at the beginning.

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def SelectioSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i+1, n):
            if(arr[j]<arr[min_idx]):
                min_idx = j
        swap(min_idx, i, arr)

array = [10, 1, 2, 6, 1, 2, 5]
SelectioSort(array)
print(array)
