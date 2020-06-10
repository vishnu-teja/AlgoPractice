
def swapValues(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def chooseRandomPivot(array, startIndex, endIndex):
    return endIndex


def arrayPartition(array, startIndex, endIndex):
    randomPivot = chooseRandomPivot(array, startIndex, endIndex)
    swapValues(array, randomPivot, endIndex)
    pivot = startIndex
    for i in range(startIndex, endIndex):
        if array[i] < array[endIndex]:
            swapValues(array, i, pivot)
            pivot += 1
    swapValues(array, pivot, endIndex)
    return pivot


def randomizedSelection(array, startIndex, endIndex):
    global ithOrderIndex
    pivot = arrayPartition(array, startIndex, endIndex)
    if pivot == ithOrderIndex:
        return array[pivot]
    elif pivot > ithOrderIndex:
        return randomizedSelection(array, startIndex, pivot - 1)
    else:
        return randomizedSelection(array, pivot + 1, endIndex)


file = open('../data/unsorted.txt', 'r')
array = list(map(int, file.readlines()))

file.close()

ithOrderIndex = 264

print(randomizedSelection(array, 0, len(array)-1))

    
    
