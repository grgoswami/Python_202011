
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
    
class TollBooth:
    def __init__(self, num_booths):
        self.num_booths = num_booths
        self.toll_charges = {
            'SEDAN': 11.75,
            'SUV': 36.0,
            'TRUCK': 54.0
            }
        
    def collect_toll(self, land_vehicles):
        """
        Parameters
        ----------
        land_vehicles : list of objects of class LandVehicle
            This take the list of all LandVehicle objects that crossed
            the toll boths.

        Returns
        -------
        The total amount of toll collected.
        """
        self.land_vehicles = land_vehicles
        total = 0.0
        for lv in self.land_vehicles:
            total += self.toll_charges[lv.kind]
        print(f'In collect_toll: total={total}')
        print('In collect_toll: total=', total)
        print('In collect_toll: total=' + str(total))
        return total
    
tb = TollBooth(1)
tb.collect_toll(lvs)
tb.collect_toll([sedan, suv, truck, sedan, suv])

            
