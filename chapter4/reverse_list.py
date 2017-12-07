"""Reversing a list recursively """
def reverse_list(arr):
    """
    Reversing a list with just one input variable
    """
    if not arr:
        return arr
    return arr[-1:] + reverse_list(arr[:-1])

print(reverse_list([9, 4, 2, 1, 2])) # Testing the above method

def reverse_list_book(arr, start, stop):
    """
    Reversing list method given in book
    """
    if start < stop - 1:
        arr[start], arr[stop - 1] = arr[stop - 1], arr[start]
        reverse_list_book(arr, start + 1, stop - 1)

LS = [9, 4, 2, 1, 2]
reverse_list_book(LS, 0, 5)
print(LS) # Testing the above method
