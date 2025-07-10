class Father:
    def speak_father(self):
        print('Father speak')
class Mother:
    def speak_mother(self):
        print('Mother speak')
class Child(Mother, Father):
    def speak_child(self):
        print('Child speak')
c=Child()
c.speak_child()
c.speak_father()
c.speak_mother()
    