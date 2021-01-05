
# Note tuples are ordered
t0 = ('New York', 10001, 45)
print(t0)

t1 = (10001, 'New York', 45)
print(t1)

print(t0 == t1)

# indexing and slicing works on tuples pretty much like lists
t0[2]
t0[1:]

# Immutability of tuples
t0[0] = 1
t0[1:] = (101, 55)

# The right side of = is called tuple packing
# The left side of = is called tuple unpacking
v0, v1, v2 = 'New York', 10001, 45
print(v0)
print(v1)
print(v2)

x0, x1, x2 = t0
print(x0)
print(x1)
print(x2)

y0, y1 = t0
print(y0)
print(y1)

# Here '_' is a special variable in python that ignores the value of it
w0, w1, _ = 'New York', 10001, 45
print(w0)
print(w1)
