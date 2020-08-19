
# this code will generate a min arr.


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.build_heap(arr)

    def heapify(self, arr, i):
        min_index = i
        lc, rc = 2*i + 1, 2*i + 2

        if lc < len(arr) and arr[lc] < arr[min_index]:
            min_index = lc

        if rc < len(arr) and arr[rc] < arr[min_index]:
            min_index = rc

        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
            self.heapify(arr, min_index)

    def build_heap(self, arr):
        start_index = len(arr)//2 - 1
        for i in range(start_index, -1, -1):
            self.heapify(arr, i)

    def get_heap(self):
        return self.arr

    def add_to_heap(self, val):
        self.arr.append(val)
        self.restore_heap_on_add(len(self.arr) - 1)

    def restore_heap_on_add(self, i):
        parent = i//2
        if self.arr[parent] > self.arr[i]:
            self.arr[parent],  self.arr[i] = self.arr[i],   self.arr[parent]
            self.restore_heap_on_add(parent)

    def pop_from_heap(self):
        if not len(self.arr):
            return None
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[-1], self.arr[0]
        val = self.arr.pop()
        self.heapify(self.arr, 0)
        return val


arr = [5, 60, 25, 11, 42, 99, 61, 13, 54, 71,
       17, 23, 39, 18, 22, 12, 43, 15, 8, 3]

print(arr)
# arr = Heap(arr)
# print(arr.get_heap())

# arr.add_to_heap(1)
# print(arr.get_heap())


# arr.pop_from_heap()
# print(arr.get_heap())

import heapq
newa = []
heapq.heapify(newa)
for i in arr:
    k = -i
    heapq.heappush(newa, -1 * k)
print(newa)