# The following is a list of dictionaries 
# List of dictionaries is essentially a row based relational database, such 
# as mysql
menu = [
        {'item': 'Pasta',
         'description': 'with sauce',
         'price': 10.0},
        {'item': 'Pizza',
         'description': 'slices',
         'price': 3.0},
        {'item': 'Garlic knots',
         'description': 'pieces',
         'price': 1.0},        
        ]
print(menu)

print(menu[1])
# [1] is list indexing by index
# ['price'] is dictionary indexing by the key
print(menu[1]['price'])

num = 1
for stuff in menu:
    print('This item: number=' + str(num) + 
          ' name=' + stuff['item'] +
          ' description=' + stuff['description'] +
          ' price=' + str(stuff['price']))
    num = num + 1

val = 100
for ri in range(5):
    print(ri)
    val = val + 1
    print(val)
    
for ri in range(4):
    print(ri)
    
x = 1
for ri in range(5):
    x = x * 2
    print(x)

x = 100
for ri in range(5):
    x = x - 5
    print(x)
    