# Problem:
# take an empty set
# add n items to the set
# take the median of the set at each iteration.
# return sum(medians)/n

# method:
# maintain high heap and low heap
# low heap is a max heap with first half of items if the set is sorted.
# high heap is a min heap with the second half of items if the set is sorted.
# for item i if i < max(low heap) it goes into low heap and viceverca
# if i > max(low heap) and i < min(max heap) then it is the median and can be added to any of the heap.

import heapq

h_low = []
h_high = []

heapq.heapify(h_high)
heapq.heapify(h_low)

file = open("./course_2/week_3/median.txt", "r")

nums = list(map(int, file.readlines()))
median_sum = 0
for n in nums:
    if not h_high or n > h_high[0]:
        heapq.heappush(h_high, n)
    elif not h_low or n < -h_low[0]:
        heapq.heappush(h_low, -n)

    else:
        heapq.heappush(h_high, n)
    if len(h_low) > len(h_high) + 1:
        heapq.heappush(h_high, -heapq.heappop(h_low))
    if len(h_high) > len(h_low) + 1:
        heapq.heappush(h_low, -heapq.heappop(h_high))
    print(h_low, h_high)
    if len(h_low) > len(h_high):
        median_sum += -h_low[0]
    elif len(h_low) < len(h_high):
        median_sum += h_high[0]
    else:
        median_sum += (-h_low[0] + h_high[0]) / 2


print(median_sum % len(nums))
