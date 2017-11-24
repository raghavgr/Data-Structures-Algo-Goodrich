""" Computes factorial of given number recursively """
def factorial(num):
    """
    Factorial of num. O(N) running time
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
