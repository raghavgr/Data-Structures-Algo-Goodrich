""" This is the book's implementation of binary search """

def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.

    """

    if low > high:                 # indicates that interval is empty, mo match found
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            print(mid)
            return True                 # found a match
        elif target < data[mid]:
            # recur on portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on portion right of the middle
            return binary_search(data, target, mid + 1, high)

print(binary_search([1, 2, 3, 4, 5], 6, 0, 4))
