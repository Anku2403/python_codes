#Bubble Sort

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def BubbleSort(array):
    n = len(array)

    for times in range(n-1):
        for j in range(n-times-1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)

array = [10, 1, 2, 5, 3, 12, 6]
BubbleSort(array)
print(array)