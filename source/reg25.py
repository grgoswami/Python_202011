
# A recursive function
def factorial1(num):
    if num == 1:
        return num
    else:
        return num * factorial1(num - 1)
    
print(factorial1(3))

print(factorial1(5))
