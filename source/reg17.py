
def Fibonacci0(num):
    """
    The following is called the docstring of the function.
    Parameters
    ----------
    num : int
        The number of elements from the Fibonacci sequence.

    Returns
    -------
    None. It prints the numbers.

    """
    a = 1
    print(a)
    b = 1
    print(b)
    for i in range(2, num):
        c = a + b
        print(c)
        a = b
        b = c

Fibonacci0(3)
Fibonacci0(5)
Fibonacci0(10)
Fibonacci0(100)
        