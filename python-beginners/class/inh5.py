class Vehicle:
    def start(self):
        print('Vehicle started')
class Bike(Vehicle):
    def ride(self):
        print('Bike ride')
class SportsBike(Bike):
    def accelerate(self):
        print('SportsBike accelerate')
c=SportsBike()
c.start()
c.ride()
c.accelerate()