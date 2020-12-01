# String indexing

str0 = 'Tista loves chocolate'
print(len(str0))

print(str0[3])

# String slicing
print(str0[5:7])

print(str0[4:7])

# String mutation
# Strings are not 'mutable'; they are called immutable
str0[3] = 'z'
print(str0)

s2 = 'New York'
zip_code = 10001

# The following is called string concatenation
print(s2 + zip_code)
print(s2 + str(zip_code))
print(s2 + ' ' + str(zip_code))

s3 = 'New York '
print(s3 + str(zip_code))
 