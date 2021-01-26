
# The arguments a and b are called positional arguments
def add0(a, b):
    return a + b

print(add0(1, 2))

print(add0(1, 100))

def add1(a, b, c):
    return a + b + c 

print(add1(1, 10, 100))
print(add1(1, 2, 3))

# In the following function *num is a variable positional argument
def addx(*nums):
    sum0 = 0
    for num in nums:
        sum0 = sum0 + num
    return sum0

print(addx(1, 2))
print(addx(1, 2, 3))
print(addx(1, 2, 3, 4, 45, 5, 100))



