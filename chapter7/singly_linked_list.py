class ListNode:
    """
    A node in a singly Linked List.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        """
        Using python's string representation method to 
        show the data present in the node.
        https://docs.python.org/3/library/functions.html#repr
        """
        return repr(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        """
        Returns a string representation of the list
        O(n) time
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'
    
    def is_empty(self):
        return self.head == None
    
    def add(self, data):
        """ 
        add to the beginning of list.
        Prepend. O(1) time
        """
        self.head = ListNode(data=data, next=self.head)
    
    def append(self, data):
        """
        Add to the end of list
        O(n) time
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)
    
    def find(self, target):
        """
        Return the first node in the linked list
        whose data==target. O(n) time
        :rtype: ListNode
        """
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        return curr
    
    def search(self, target):
        """
        similar to find but returns True if target is
        present as data in one of the nodes of a LL.
        O(n) time
        :rtype: Boolean
        """
        curr = self.head
        found = False
        while curr and not found:
            if curr.data == target:
                found = True
            else:
                curr = curr.next
        return found
    
    def remove(self, target):
        """
        Remove the node with given value
        O(n) time
        """
        curr = self.head
        prev = None
        found = False
        while curr and not found:
            if curr.data == target:
                found = True
            else:
                prev = curr
                curr = curr.next
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
            curr.next = None
        
obj = SinglyLinkedList()