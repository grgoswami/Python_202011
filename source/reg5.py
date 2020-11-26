cars = ['Toyota', 'Honda', 'Mazda']
print(type(cars))
print(cars)

# Indexing
# Indexing starts with 0 in Python at the start of the list
# Indexing starts with -1 in Python at the end of the list
print(cars[1])
print(cars[-1])
print(cars[-2])
print(cars[-3])
print(cars[-4])
print(cars[10])
print(cars[2])

ice_creams = ['vanilla', 'chocolate', 'butter pecan', 'rocky road']
print(ice_creams[-2])
print(ice_creams[2])

l0 = [3, 4]
print(l0)

l1 = ['3', '4']
print(l1)

l2 = [3, '4']
print(l2)

l3 = [3, '4', 5.91]
print(l3)

l4 = [3, -10, -5.34, '4', 5.91, 'New York']
print(l4)

# Slicing 
# Slicing looks like start:end or start: or :end or :
# The end is never touched in Python 
# start you touch, end you don't
print(cars)
print(cars[1:3])
print(cars[1:])
print(cars[:2])
# The following is called a copy of a list
print(cars[:])

ice_creams = ['vanilla', 'chocolate', 'butter pecan', 'rocky road']
print(ice_creams[:-2])
print(ice_creams[-2:])
print(ice_creams[-4:-1])
print(ice_creams[-3:-2])
print(ice_creams)

# Note, lists are called 'mutable'
# list assignment
ice_creams[1] = 'strawberry'
print(ice_creams)

ice_creams[-2] = 'peach'
print(ice_creams)

ice_creams[3] = 'raspberry'
print(ice_creams)








