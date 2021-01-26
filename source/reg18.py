# A function may or may not return an object, it entirely depends on the
# implementor of the function
def Fibonacci1(num):
    """
    Parameters
    ----------
    num : int
        The number of elements from the Fibonacci sequence.

    Returns
    -------
    The sequence.

    """
    ret = []
    a = 1
    ret.append(a)
    b = 1
    ret.append(b)
    for i in range(2, num):
        c = a + b
        ret.append(c)
        a = b
        b = c
    return ret

nums0 = Fibonacci1(3)
print(nums0)

ret1 = Fibonacci1(5)
print(ret1)

vals0 = Fibonacci1(10)
fib0 = Fibonacci1(100)
        