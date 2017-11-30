""" Implement find unique element recursively """

def unique_recur(arr):
    """ Good recursive find unique element implementation """
    if len(arr) == 1:
        return True
    else:
        curr_element = arr[0]
        rest_of_arr = arr[1:]
        elem_is_unique = curr_element not in rest_of_arr
        recur = unique_recur(rest_of_arr)
        return elem_is_unique and recur

print(unique_recur([1, 3, 2, 4]))

def bad_unique(arr, start, stop):
    """ Bad recursive implementation of find unique element """
    if stop - start <= 1: 
        return True   # only one item
    elif not bad_unique(arr, start, stop - 1): 
        return False
    elif not bad_unique(arr, start + 1, stop):
        return False
    else:
        return arr[start] != arr[stop-1]
