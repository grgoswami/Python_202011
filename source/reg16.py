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

for ci in range(len(menu)):
    print(str(ci) + ' -- ' + menu[ci]['item'] + ' | ' + str(menu[ci]['price'])) 

# When you need both the index and the elements of a list or a tuple
# you need to use enumerate
for ci, element in enumerate(menu):
    print(str(ci) + ' -- ' + element['item'] + ' | ' + str(element['price']))
    
# When you don't need the index of the list or the tuple you don't
# need to use enumerate, the regular for loop should work    
for element in menu:
    print(element['item'] + ' | ' + str(element['price']))

# The following is called string formatting, it makes second for loop above 
# much shorter        
for ci, element in enumerate(menu):
    print('{0} -- {1} | {2}'.format(ci, element['item'], element['price']))
    
for element in menu:
    print('{0} | {1}'.format(element['item'], element['price']))
    
    
    