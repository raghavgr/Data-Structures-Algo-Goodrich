"""" Binary Search implementation """
def binary_search(data, target, low, high):
    """
    data: the sorted list from which we need to find target
    target: the element we are searching for
    low: current lowest index to search upto
    high: current highest index to search upto
    
    Return True and prints the index point where the target is located
    """
    mid = (low + high) // 2
    if data[mid] == target:
        print(mid)
        return True
    elif target < data[mid]:
        binary_search(data, target, low, mid - 1)
    else:
        binary_search(data, target, mid + 1, high)

print(binary_search([1, 2, 3, 4, 5], 3, 0, 4))
