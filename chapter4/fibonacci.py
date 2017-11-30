""" Recursive implementations of nth fibonacci number
        F(0) = 0
        F(1) = 1
        F(n) = F(n-2) + F(n - 1) """
def bad_fibonacci(num):
    """ bad implementation """
    if num <= 1:
        return num    # F(0) & F(1)
    else:
        return bad_fibonacci(num - 2) + bad_fibonacci(num - 1)

def fibonacci(num):
    