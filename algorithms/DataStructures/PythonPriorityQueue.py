class PriorityQueueEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        entry = PriorityQueueEntry(item, priority)
        self.queue.append(entry)

    def dequeue(self):
        assert not self.is_empty(), "PriorityQueue is empty."
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i].priority > self.queue[max].priority:
                max = i

        entry = self.queue[max]
        del self.queue[max]
        return entry.item


q = PriorityQueue()
q.enqueue("test", 1)
q.enqueue("test2", 2)
q.enqueue("test3", 3)
q.enqueue("test4", 4)
q.enqueue("test5", 5)
q.enqueue("test6", 6)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())