def unique1(ls):
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[i] == ls[j]:
                return False

    return True

print(unique1([1, 2, 1, 3]))


def unique2(ls):
    """ Better unique implementation """
    temp = sorted(ls)
    for i in range(1, len(temp)):
        if temp[i - 1] == temp[i]:
            return False
    return True

print(unique2([1, 2, 1, 2]))