class Painter:
    def talent(self):
        print('Hello Painter')
class Musician:
    def talent(self):
        print('Hello Musician')
class Artist(Painter, Musician):
    def talent(self):
        super().talent()
        print('Hello Artist')
c=Artist()
c.talent()
