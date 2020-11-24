
# Ages of my siblings are 8, 3
ages_of_siblings = '8,3'
print(ages_of_siblings.split(','))

ages = ages_of_siblings.split(',')
print(ages)

# Here pretty printing makes strings look like
for age in ages:
    print(age)

for banana in ages:
    print(banana)
    
for i in ages:
    print(i)
    
for age in ages:
    print(int(age))
    
str0 = '100'
print(str0)

# The int funcion converts a str into an int
int0 = int(str0)
print(int0)

# The type function below gives you the type of the variable or object
type(str0)
type(int0)

weights_of_siblings = '89.1,27.3'
weights = weights_of_siblings.split(',')
print(weights)

weights_of_siblings1 = '90.3;50.7;57.8'
weights1 = weights_of_siblings1.split(';')
print(weights1)

str1 = 'My name is Jane Doe'
words = str1.split(' ')
print(words)

str2 = 'Thanksgiving and Christmas and New Year'
holidays1 = str2.split('and')
print(holidays1)
holidays2 = str2.split(' and ')
print(holidays2)

for hol in holidays2:
    print(hol)
    print('This holidays is: ' + hol)

print(' -- '.join(holidays2))
print(' | '.join(holidays2))
print('; '.join(holidays2))

print(float('4.0') + 5)

print('Jane' + 'Doe')
print('Jane ' + 'Doe')


    