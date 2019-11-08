import math
from functools import total_ordering

@total_ordering
class heap_node:
    def __init__(self, v1, v2, priority):
        self.v1 = v1
        self.v2 = v2
        self.priority = priority
    # Overloads comparison operators so we can compare heap nodes directly 
    # based on their priority
    def __eq__(self, other):
        return self.priority == other.priority

    def __ne__(self, other):
        return self.priority != other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return "({}) {}".format(self.priority, self.label)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return math.floor(i / 2)

class Heap:
    def __init__(self, arr=[]):
        self.heap = [heap_node(*x) for x in arr]
        # if an array is provided heapify it 
        if self.heap:
            self.build_heap()

    def __repr__(self):
        return ' | '.join(map(str, self.heap))

    def __len__(self):
        return len(self.heap)

    def build_heap(self):
        sz = len(self.heap)
        i = math.floor(sz / 2)
        while i >= 0:
            self.heapify(i)
            i -= 1

    def delete_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()
        self.heapify(0)
        return ret.v1, ret.v2, ret.priority

    def heapify(self, i):
        l = left(i)
        r = right(i)
        sz = len(self.heap) - 1
        if l <= sz and self.heap[l] < self.heap[i]:
            smallest = l
        else:
            smallest = i
        
        if r <= sz and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def insert(self, vals):
        self.heap.append(heap_node(*vals))
        index = len(self.heap) - 1
        p = parent(index)
        while index > 0 and self.heap[index] < self.heap[p]:
            self.heap[index], self.heap[p] = self.heap[p], self.heap[index]
            index = p
            p = parent(p)

    def verify_heap(self):
        for i in range(len(self.heap) // 2):
            if left(i) < len(self.heap):
                if self.heap[i] > self.heap[left(i)]:
                    return False
            if right(i) < len(self.heap):
                if self.heap[i] > self.heap[right(i)]:
                    return False
        return True
