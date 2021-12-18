# Binary Search algorithm - It works only for Sorted array.
def BinSearch(arr, x):
    s = 0
    e = len(arr) - 1

    while(s<=e):
        mid = (s+e) // 2
        if arr[mid] < x:
            s = mid + 1
        elif arr[mid] > x:
            e = mid - 1
        else:
            return mid

    return -1

arr = [2, 3, 4, 10, 40]
x = int(input("Enter the number to search in array: "))

idx = BinSearch(arr, x)
if idx == -1:
    print("Element is not present in array")
else:
    print(x, "Element present at Index", idx)