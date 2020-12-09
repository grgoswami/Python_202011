
colors = {
    'Tista': 'Purple',
    'Gia' : 'Turquoise',
    'Anya':'Minty Green'
    }

print(colors)
for name , color in colors.items():
    print(name + "'s favorite color is " + color)
    print(name + ' has ' + str(len(name)) + ' letters in her or his name')
    print('\n')
    
    
#Survey

name1 = input("What's your name ?  ")
color1 = input('Favorite Color : ')

name2 = input("What's your name ?  ")
color2 = input('Favorite Color : ')

name3 = input("What's your name ?  ")
color3 = input('Favorite Color : ')

survey = {
    name1: color1,
    name2: color2,
    name3: color3
    }

print('\n')

for name, color in survey.items():
    print(name + "'s favorite color is " + color)
    print(name + ' has ' + str(len(name)) + ' letters in her name')
    print('\n')