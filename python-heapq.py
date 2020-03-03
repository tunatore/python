import heapq

list = [10, 7, 9, 1, 4]
heapq.heapify(list)
print("heap:", list)
heapq.heappush(list, 6)
print("heap: ", list)

print("heap smallest item:", heapq.heappop(list))
print("nlargest: ", heapq.nlargest(2, list))
print("nsmallest: ", heapq.nsmallest(2, list))
