class Person:
    def __init__(self, name, age, occupations, health_conditions):
        self.name = name
        self.age = age
        self.occupations = occupations
        self.health_conditions = health_conditions
        
    def describe(self):
        print(f'The person being analyzed is {self.name}')
        print(f'The age of the person is {self.age}')
        print("The occupations that the person has is {0}".format(', '.join(self.occupations)))
        print("The health conditions that the person has is {0}".format(', '.join(self.health_conditions)))

p1 = Person("John Doe", 50, ['Finance', 'Consulting'], ['BP', 'Diabetes',
    'Obesity', 'extreme stupidity',     'anoyingness', ])
p1.describe()

p100 = Person("Zubin the Anvit the Attie", 78, ['Farting Consulter', 'Consulting'], 
['BP', 'Diabetes', 'Obesity', 'extreme stupidity', 'extreme anoyingness', ])
p100.describe()

p2 = Person("Jane Doe", 17, ['Doctor', 'Consulting'], 
['BP', 'Diabetes', 'Obesity', 'extreme stupidity', 'extreme anoyingness', ])
p2.describe()

class Vaccination:
    def __init__(self, minimun_age):
        self.minimun_age = minimun_age
    
    def assign_priority(self, person):
        if person.age >= self.minimun_age:
            print(f"{person.name}, you are a higher priority")
        else:
            print(f"{person.name}, you are a lower priority")
            
v0 = Vaccination(65)
v0.assign_priority(p1)
v0.assign_priority(p100)

l0 = [p1, p2, p100]
for person in l0:
    v0.assign_priority(person)
    
    