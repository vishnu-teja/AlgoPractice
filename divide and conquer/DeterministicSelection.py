


def swapValues(arr, i, j):
  t = arr[i]
  arr[i]=arr[j]
  arr[j] = t


def chooseDeterministicPivot(array, startIndex, endIndex):
  subArr = array[startIndex: endIndex]
  if len(subArr) <= 5:
    sortedArr = sorted(subArr)
    mid =   len(sortedArr) // 2 
    return (startIndex + subArr.index(sortedArr[mid]), sortedArr[mid])
  medians = []
  i = startIndex
  while i <= endIndex:
    if i+5 <= endIndex:
      medians.append(chooseDeterministicPivot(array, i, i + 5))
    else:
      medians.append(chooseDeterministicPivot(array, i, endIndex + 1));
    i += 5
  medians = sorted(medians, key = lambda x: x[1])

  mid = len(medians) // 2
  return medians[mid]



def  arrayPartition(array, startIndex, endIndex):
  (randomPivot, val) = chooseDeterministicPivot(array, startIndex, endIndex)
  swapValues(array, randomPivot, endIndex)
  pivot = startIndex
  for i in range(startIndex, endIndex):
      if array[i] < array[endIndex]:
          swapValues(array, i, pivot)
          pivot += 1
  swapValues(array, pivot, endIndex)
  return pivot


def deterministicSelection(array, startIndex, endIndex):
  global ithOrderIndex
  if(startIndex == endIndex):
    return array[startIndex]
  pivot = arrayPartition(array, startIndex, endIndex)
  if pivot == ithOrderIndex:
      return array[pivot]
  elif pivot > ithOrderIndex:
      return deterministicSelection(array, startIndex, pivot - 1)
  else:
      return deterministicSelection(array, pivot + 1, endIndex)



array = [8, 4, 33, 2, 55, 1, 77, 21, 65, 10, 34, 54, 22, 76, 12, 44, 11, 13]
print(sorted(array))

ithOrderIndex = None

for i in range(len(array)):
  ithOrderIndex =  i
  print(deterministicSelection(array, 0, len(array)-1))
