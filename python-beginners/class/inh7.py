class Parent:
    def speak(self):
        print('Parent speak')
class Child(Parent):
    def speak(self):
        print('Child speak')
class Father(Child):
    def speak(self):
        super().speak()
        print('Father speak')
a=Father()
a.speak()
