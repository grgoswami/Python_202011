
# Python is one of the most popular languages:
# https://www.tiobe.com/tiobe-index/

# Guido van Rossum invented Python
# https://www.youtube.com/watch?v=J0Aq44Pze-w

# Python GitHub links:
# https://github.com/python/cpython/

# Example Python file
# https://github.com/python/cpython/blob/master/Lib/urllib/response.py

# Example C file
# https://github.com/python/cpython/blob/master/Python/getargs.c

# [] is called squre braces
# () is called parenthses
names = ['Sidd', 'Advik', 'Vikrant']
for name in names:
    print(name)

student_info = [('Sahana', 'girl'), ('Anvit', 'boy'), ('Attie', 'girl')]
for name, gender in student_info:
    print(name + ' is a ' + gender)

# {} is called curly braces   
student_preferences = {
    'Ethen': ['French fries'],
    'Reha': ['Mac n cheese'],
    'Ridhima': ['Apple'],
    'Veda': ['Chicken', 'Ceaser salad'],
    'Zubin': ['Mac n cheese', 'Burger'],
    'Alisha': ['Chicken']
    }
for name, foods in student_preferences.items():
    print(name + ' likes ' + ' & '.join(foods))
    
    