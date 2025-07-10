class Employeee:
    def work(self):
        print('Working')
class Developer(Employeee):
    def work(self):
        super().work()
        print('Writing code')
c=Developer()
c.work()
