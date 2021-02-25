
class Car:
    def __init__(self, brand, kind, color):
        """
        This is the constructor of the class.

        Parameters
        ----------
        brand : str
            Brand of the car.
        kind : str
            Kind of the car, e.g., sedan, SUV, minivan.
        color : str
            Color of the car.

        Returns
        -------
        None.

        """
        self.brand = brand
        self.kind = kind
        self.color = color
        
    def describe(self):
        print('This car: {0} | {1} | {2}'.format(self.brand, self.kind, self.color))
        
    def drive(self, start, end):
        print(f"Ok: I'm going to drive you from {start} to {end}")
        
# Create or instantiate or construct objects from the class Car as follow 
# car0 is an object of the class Car
car0 = Car('Ford', 'Truck', 'White')
car0.describe()
car0.drive('Short Hills', 'New York')

car1 = Car('Toyota', 'Sedan', 'Red')
car1.describe()
car1.drive('Short Hills', 'New York')

car2 = Car('Mazda', 'Sports car', 'Yellow')
car2.describe()
car2.drive('Short Hills', 'New York')


        
        