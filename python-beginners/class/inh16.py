class Appliance:
    def turn_on(self):
        print('turn on')
class WashingMachine(Appliance):
    def turn_on(self):
        super().turn_on()
        print('Washing Machine')
class Microwave(WashingMachine):
    def turn_on(self):
        super().turn_on()
        print('Microwave')
on=Microwave()
on.turn_on()
