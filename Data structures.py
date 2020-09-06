



"""
Trees
"""

"""
Heap
"""

"""
Stack
- LIFO
"""
class StackNode:
    def init(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self, data):
        self.data = data
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, data):
        node = StackNode(data)
        if self.size != 0:
            node.next = self.top
        self.top = node
        self.size += 1
    def pop(self):
        if self.size > 0:
            ret = self.top.data
            self.top = self.top.next
            self.size -= 1


"""
Queues and Priority Queues
- FIFO
- Sorted or unsorted based on priority (value or time added)
"""


"""
Linked List

- Single, double, circular linkages
- Each node points to another (except tail unless double/circular)
- Pointers for head and tail
- Sorted or unsorted list
"""


"""
Hash table
"""

"""
Array
- Fixed size
"""