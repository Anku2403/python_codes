def partition(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

def quickSort(arr,left,right):
    if left < right:
        partition_pos = partition(arr,left,right)
        quickSort(arr, left, partition_pos - 1)
        quickSort(partition_pos + 1, right)

arr = [22,11,88,66,55,77,33,44]
n = len(arr) - 1
quickSort(arr,0,n)
print(arr)
