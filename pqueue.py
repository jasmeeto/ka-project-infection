# Generic Priority queue class taken from http://stackoverflow.com/a/407922

import heapq

class PriorityQueue(object):
    """
    Combined priority queue and set data structure.

    Acts like a priority queue, except that its items are guaranteed to be
    unique. Provides O(1) membership test, O(log N) insertion and O(log N)
    removal of the smallest item.

    Important: the items of this data structure must be both comparable and
    hashable (i.e. must implement __cmp__ and __hash__). This is true of
    Python's built-in objects, but you should implement those methods if you
    want to use the data structure for custom objects.
    """

    def __init__(self, items=[]):
        """
        Create a new PriorityQueue.

        Arguments:
            items (list): An initial item list - it can be unsorted and
                non-unique. The data structure will be created in O(N).
        """
        self.set = dict((item, True) for item in items)
        self.heap = self.set.keys()
        heapq.heapify(self.heap)
        self.counter=0

    def has_item(self, item):
        """Check if ``item`` exists in the queue."""
        return item in self.set

    def pop_smallest(self):
        """Remove and return the smallest item from the queue."""
        smallest = heapq.heappop(self.heap)
        del self.set[smallest[2]]
        return smallest[0], smallest[2]

    def add(self, item, priority):
        """Add ``item`` to the queue if doesn't already exist."""
        if item not in self.set:
            self.set[item] = True
            heapq.heappush(self.heap, (priority, self.counter, item))
            self.counter+=1

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def size(self, priority):
        return sum(1 for i in self.heap if i[0] == priority)