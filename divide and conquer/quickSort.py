import random

a = [6, 3, 4, 2, 1, 8, 9, 2, 33, 11, 66, 6, 222, 77, 88, 444, 333, 45]


def swapData(a, i, j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp


def partition(a, f, l):
  rand = random.randrange(f, l + 1)
  pivot = f
  swapData(a, rand, l)
  for i in range(f, l):
    if i != l and a[i] < a[l]:
      swapData(a, i, pivot)
      pivot+=1 
  swapData(a, pivot, l)
  return pivot


def quickSort(a, f, l):
  if f < l:
    pi = partition(a, f, l)
    quickSort(a, f, pi - 1)
    quickSort(a, pi+1, l)
  


print(a)
quickSort(a, 0, len(a)-1)

print(a)
