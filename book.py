class Book:
    def __init__(self, id, title, author, year):
        # year being the year the book was published
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        print(f'Book("{self.title}", "{self.author}", "{self.year}")')

    def __str__(self):
        return f'This book is titled {self.title}, authored by {self.author} and published in {self.year}'

book1 = Book(1, "The fault in our stars", "John Green", 2012)
print(book1)
print(book1.__repr__())