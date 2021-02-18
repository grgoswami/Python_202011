# Lambda functions

ret = map(lambda x: x * x, [1, 2, 3])
print(list(ret)) 

ret1 = map(lambda x: x * x * x, [1, 2, 3])
print(list(ret1)) 

def cube(x):
    return x * x * x

ret2 = map(cube, [1, 2, 3])
print(list(ret2)) 

ret3 = map(lambda x: x * x * x, (1, 2, 3))
print(list(ret3)) 

# map is called second order function, it applies the function to each
# element of the list or tuple or dictionary

ret3 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(ret3)) 

ret4 = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6])
print(list(ret4)) 

# filter is also called second order function, it applies the function to each
# each element of the list or tuple or dictionary and returns only the 
# elements for which the functions returns True
