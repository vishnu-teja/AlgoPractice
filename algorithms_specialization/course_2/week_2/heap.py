
# this code will generate a min heap.


def heapify(heap, i):
    min_index = i
    lc, rc = 2*i + 1, 2*i + 2

    if lc < len(heap) and heap[lc] < heap[min_index]:
        min_index = lc

    if rc < len(heap) and heap[rc] < heap[min_index]:
        min_index = rc

    if min_index != i:
        heap[min_index], heap[i] = heap[i], heap[min_index]
        heapify(heap, min_index)


def build_heap(arr):
    start_index = len(arr)//2 - 1
    for i in range(start_index, -1, -1):
        heapify(arr, i)


heap = [5, 2, 11, 9, 6, 13, 7, 1, 23, 18, 22, 12, 4, 15, 8, 3]

print(heap)
build_heap(heap)
print(heap)
