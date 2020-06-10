
def swapValues(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    
    
#    median of first, middle and last values of the array is chosen as random pivot
def chooseRandomPivot(array, startIndex, endIndex):
    mid = (endIndex - startIndex) // 2
    return sorted([(startIndex, array[startIndex]), (mid, array[mid]), (endIndex, array[endIndex])], key = lambda x: x[1])[1][0]


def arrayPartition(array, startIndex, endIndex):
    randomPivot = chooseRandomPivot(array, startIndex, endIndex)
    swapValues(array, randomPivot, endIndex)
    
    pivot = startIndex
    
    for i in range(startIndex, endIndex):
        if array[i] < array[endIndex]:
            swapValues(array, pivot, i)
            pivot += 1
    swapValues(array, pivot, endIndex)
    return pivot


def quickSort(array, startIndex, endIndex):
    if startIndex < endIndex:
        pivot = arrayPartition(array, startIndex, endIndex)
        quickSort(array, startIndex, pivot - 1)
        quickSort(array, pivot + 1, endIndex)

    



file = open('../data/unsorted.txt', 'r')
array = list(map(int, file.readlines()))

file.close()

quickSort(array, 0, len(array) - 1)

print(array)
