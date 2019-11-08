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
    ''' Returns left child of node i '''
    return 2 * i + 1

def right(i):
    ''' Return right child of node i '''
    return 2 * i + 2

def parent(i):
    ''' Return the parent of node i '''
    return math.floor(i / 2)

class Heap:
    def __init__(self, arr=[]):
        self.heap = [heap_node(*x) for x in arr]
        # if an array is provided heapify it 
        if self.heap:
            self.build_heap()

    def __repr__(self):
        return ' | '.join(map(str, self.heap))

    # overlead len() call on a Heap object
    def __len__(self):
        return len(self.heap)

    def build_heap(self):
        ''' create a heap from an unordered array with bottom-up method '''
        i = math.floor(len(self) / 2)
        while i >= 0:
            self.heapify(i)
            i -= 1

    def delete_min(self):
        ''' 
        removes and returns the minimum priority node from the heap 
        while maintaining the heap and shape properties 
        '''
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()
        self.heapify(0)
        return ret.v1, ret.v2, ret.priority

    def heapify(self, i):
        '''
        For node i that roots child heaps enforces the heap property
        '''
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
        '''
        Inserts a new tuple into the heap and moves into the correct position to maintain
        the heap and shape properties
        '''
        self.heap.append(heap_node(*vals))
        index = len(self.heap) - 1
        p = parent(index)
        # Bubble up the new node until the heap property is satisfied
        while index > 0 and self.heap[index] < self.heap[p]:
            self.heap[index], self.heap[p] = self.heap[p], self.heap[index]
            index = p
            p = parent(p)

    def verify_heap(self):
        '''
        Verifies that this is in fact a Min-Heap. If the child of any parent
        is smaller than it then returns False.
        Returns True otherwise.
        '''
        for i in range(len(self.heap) // 2):
            if left(i) < len(self.heap):
                if self.heap[i] > self.heap[left(i)]:
                    return False
            if right(i) < len(self.heap):
                if self.heap[i] > self.heap[right(i)]:
                    return False
        return True
