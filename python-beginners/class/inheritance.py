class father:
    def speak(self):
        print("I am father")
class mother:
    def talk(self):
        print("I am mother")
class son(father,mother):
    pass
c=son()
c.speak()
c.talk()