
# Dictionary is a collection of pair of key and value
# The following is a dictionary of lists
# Pandas data frame is essentially a dictionary of lists
# This is also used in column based databases such as Kdb
menu = {
        'items': ['Pasta', 'Pizza', 'Garlic knots'],
        'description': ['with sauce', 'slices', 'pieces'],
        'prices': [10.0, 3.0, 1.0]
        }
print(menu)

print(menu['items'])
print(menu['items'][1])
number_items = len(menu['items'])
print(number_items)

for limit in range(-1, 5):
    print(limit)

for di in range(number_items):
    print('This item: number=' + str(di + 1) + ' name=' + menu['items'][di] +
          ' description=' + menu['description'][di] +
          ' price=' + str(menu['prices'][di]))
    