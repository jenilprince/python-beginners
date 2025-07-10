class Bird:
    def fly(self):
        print('Bird fly')
class Parrot(Bird):
    def speak(self):
        print('Parrot speak')
c=Parrot()
c.fly()
c.speak()