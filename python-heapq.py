import heapq

list = [10, 7, 9, 1, 4]
heapq.heapify(list)
print("heap:", list)
heapq.heappush(list, 6)
print("heap: ", list)

print("heap smallest item:", heapq.heappop(list))
print("nlargest: ", heapq.nlargest(2, list))
print("nsmallest: ", heapq.nsmallest(2, list))

heap_list = []
heapq.heappush(heap_list, (4, "test4"))
heapq.heappush(heap_list, (5, "test5"))
heapq.heappush(heap_list, (6, "test6"))
heapq.heappush(heap_list, (1, "test1"))
heapq.heappush(heap_list, (2, "test2"))
heapq.heappush(heap_list, (3, "test3"))

print("\nheap:")
while heap_list:
    print(heapq.heappop(heap_list))

heap_list = []
heapq.heappush(heap_list, 6)
heapq.heappush(heap_list, 7)
heapq.heappush(heap_list, 8)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 2)
heapq.heappush(heap_list, 3)

print()
print("heap:")
while heap_list:
    print(heapq.heappop(heap_list))
