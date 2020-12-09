colors = {
    'Tista': ['Purple', 'her'],
    'Gia' : ['Turquoise', 'her'],
    'Anya':['Minty Green', 'her'],
    'Zubin' : ['Orange', 'his'],
    'Adhvik' : ['Green', 'his']
    }

print(colors)
for name , info in colors.items():
    print(name + "'s favorite color is " + info[0])
    print(name + ' has ' + str(len(name)) + ' letters in ' + info[1] + ' name')
    print('\n')