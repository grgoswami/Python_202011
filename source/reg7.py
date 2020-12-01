
s0 = str(100)
print(s0)

s1 = str(100.01)
print(s1)

items = ['Apple', 'Orange', 'Banana', 'Strawberry', 'Pumpkin']
prices = [1.25, 0.75, 0.25, 0.35, 2.0]

print(range(5))
print(list(range(5)))
print(list(range(3)))
print(list(range(7)))
print(len(items))
print(list(range(len(items))))

for li in range(len(items)):
    print('This item: number=' + str(li + 1) + ', name=' + items[li] + 
          ', price=' + str(prices[li]))

for li in range(len(items)):
    print('This item: number =  1, name = Apple' + items[li] + 
          ', price = ' + str(prices[li]))
     
    
