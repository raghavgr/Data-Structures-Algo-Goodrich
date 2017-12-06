def linear_sum(arr, n):
    """ Return sum of sequence arr until n numbers """
    if n == 0:
        return 0
    else:
        return arr[n-1] + linear_sum(arr, n-1)

arr = [4, 3, 6, 2, 8]
print(linear_sum(arr, len(arr)))
