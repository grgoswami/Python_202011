def weighted_average(values, weights):
    """
    Parameters
    ----------
    values : list of floats or ints
        The values for which we need the weighted average.
    weights : list of floats or ints
        The weights associated with the values.

    Returns
    -------
    The weighted average of the values weighted by the weights.
    Please use a website like the one below to learn more on 
    weighted average:
        
        https://www.mathsisfun.com/data/weighted-mean.html
    """
    sum0 = 0.0
    for it in range(len(values)):
        sum0 += (values[it] * weights[it])        
    return sum0

print(weighted_average([1, 2, 3, 4], [0.1, 0.1, 0.7, 0.1]))
print(weighted_average([1, 2, 3, 4], [1/4, 1/4, 1/4, 1/4]))
print(weighted_average([1.9, 2.5, 3.1, 4.3], [1/4, 1/4, 1/4, 1/4]))
