class ArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage. """

    def __init__(self):
        """Create an empty stack"""
        self._data = []
    
    def __len__(self):
        """ Return the number of elements in the stack. """
        return len(self._data)

    def is_empty(self):
        """ Return True if stack is empty. """
        return len(self._data) == 0
    
    def push(self, e):
        """ Add element to the top of the stack. """
        self._data.append(e)
    
    def top(self):
        """ Return (but do not remove) the element at the
        top of the stack. Raise exception if empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """
        Remove and return the element from top of the stack. (LIFO)
        Raise exception if stack is empty
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()                 # remvoe last item of list

obj = ArrayStack()
obj.push(4)
obj.push(6)
print(obj.pop())
obj.top()
