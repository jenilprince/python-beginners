class ElectronicDevice:
    def power_on(self):
        print('Electronic device power on')
class Computer(ElectronicDevice):
    def boot(self):
        print('Computer booted')
class Laptop(Computer):
    def fold(self):
        print('Laptop fold')
c=Laptop()
c.power_on()
c.boot()
c.fold()