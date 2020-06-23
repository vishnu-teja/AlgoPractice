# breaking an array into 2 parts and merging them back in order.


def mergeArrays(array, startIndex, mid, endIndex):
    leftArray = array[startIndex: mid]
    rightArray = array[mid: endIndex]
    li = ri = 0
    for i in range(startIndex, endIndex):
        if (li < len(leftArray) and (ri >= len(rightArray) or leftArray[li] <= rightArray[ri])):
            array[i] = leftArray[li]
            li += 1
        elif (ri < len(rightArray) and (li >= len(leftArray) or leftArray[li] > rightArray[ri])):
            array[i] = rightArray[ri]
            ri += 1
        i += 1


def mergeSort(array, startIndex, endIndex):
    if len(array[startIndex: endIndex]) > 1:
        mid = startIndex + (endIndex - startIndex) // 2
        mergeSort(array, startIndex, mid)
        mergeSort(array, mid, endIndex)
        mergeArrays(array, startIndex, mid, endIndex)


# read data from file
# file = open('../data/unsorted.txt', 'r')
# array = list(map(int, file.readlines()))
# file.close()


array = [1, 19, 10, 20, 2, 21, 11, 22, 3, 23, 12, 24, 4, 25,  13, 26, 5,
         27, 14, 28, 6, 29, 15, 30, 7, 31, 16, 32, 8, 33, 17, 34, 9, 35, 18, 37]

mergeSort(array, 0, len(array))

print(array)
