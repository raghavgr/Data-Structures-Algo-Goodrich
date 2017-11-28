""" Three implementations of find unique element in an array """

def unique1(arr):
    """ brute force implementation """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return False

    return True

print(unique1([1, 2, 1, 3]))


def unique2(arr):
    """ Better unique implementation """
    temp = sorted(arr)
    for i in range(1, len(temp)):
        if temp[i - 1] == temp[i]:
            return False
    return True

print(unique2([1, 2, 1, 2]))
