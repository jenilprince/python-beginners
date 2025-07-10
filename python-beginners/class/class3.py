class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Pages:",self.pages)
b1=Book("My Python Book","ab",10)
b2=Book("My Python Book","ac",20)
b1.display()
b2.display()