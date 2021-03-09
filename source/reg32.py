
class LandVehicle:
    def __init__(self, kind, make, color, license_plate):
        self.kind = kind
        self.make = make
        self.color = color
        self.license_plate = license_plate
        
    def describe(self):
        print(f'This LandVehicle: kind={self.kind} make={self.make} color={self.color} license_plate={self.license_plate}')
        
sedan = LandVehicle('SEDAN', 'Honda', 'Red', 'ABC123')
suv = LandVehicle('SUV', 'Toyota', 'White', 'DEF456')
truck = LandVehicle('TRUCK', 'Ford', 'Blue', 'XYZ789')

sedan.describe()
suv.describe()
truck.describe()

lvs = [sedan, suv, truck]
for lv in lvs:
    lv.describe()
    

