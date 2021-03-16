class Person:
    def __init__(self, name, age, occupations, health_conditions):
        self.name = name
        self.age = age
        self.occupations = occupations
        self.health_conditions = health_conditions
        
    def describe(self):
        print(f'The person being anylized is {self.name}')
        print(f'The age of the person is {self.age}')
        print("The occupations that the person has is {0}".format(', '.join(self.occupations)))
        print("The health conditions that the person has is {0}".format(', '.join(self.health_conditions)))

p1 = Person("John Doe", 50, ['Finance', 'Consulting'], ['BP', 'Diabetes',
                                                        'Obesity', 'extreme stupidity', 'anoyingness', ])
p1.describe()

