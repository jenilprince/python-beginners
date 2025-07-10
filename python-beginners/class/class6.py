class Movie:
    def __init__ (self, title, director, rating):
        self.title=title
        self.director=director
        self.rating=rating
    def display(self):
        print(self.title, self.director, self.rating)
m1=Movie("m1", "d1", 5)
m2=Movie("m2", "d2", 4)
m1.display()
m2.display()