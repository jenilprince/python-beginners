class Vehicle:
    def start(self):
        print('Starting')
class Car(Vehicle):
    def drive(self):
        print('Driving')
c=Car()
c.drive()
c.start()
