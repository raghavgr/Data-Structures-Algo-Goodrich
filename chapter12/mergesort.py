"""
DSGoodrich implementation of merge sort
"""
def merge_sort(arr):
    """
    Divide the array and sort it
    """
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)

def merge(arr, left, right):
    """
    Merge two sorted lists, left and right into one of size len(arr)
    """
    i = j = 0
    while i + j < len(arr):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1

A_LIST = [65, 47, 34, 21, 55, 21, 10]
merge_sort(A_LIST)
print(A_LIST)
