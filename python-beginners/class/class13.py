class Calculator:
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def add(self):
        add=self.a+self.b
        print(add)
    def sub(self):
        sub=self.a-self.b
        print(sub)
    def mul(self):
        mul=self.a*self.b
        print(mul)
    def div(self):
        div=self.a/self.b
        print(div)
    def display(self):
        print(self.a,self.b)
num=Calculator(1,2)
num.display()
num.add()
num.sub()
num.mul()
num.div()