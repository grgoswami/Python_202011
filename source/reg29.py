foods = {
    'pepper': 'spicy',
    'ice cream': 'sweet'
    }
print(foods)

def taste0(item, taste):
    # The foods variable is local to the function's scope
    foods = {}
    foods[item] = taste
    return foods

t0 = taste0('banana', 'sweet')
print(t0)

def taste1(item, taste):
    # The foods variable is not local to the function's scope,
    # we are using the global variable
    global foods
    foods[item] = taste
    return foods

t1 = taste1('apple', 'sour')
print(t1)
