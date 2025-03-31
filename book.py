class Book:
    def __init__(self, title, author, year):
        # year being the year the book was published
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        print(f'Book("{self.title}", "{self.author}", "{self.year}")')

    def __str__(self):
        print(f'This book is titled {self.title}, authored by {self.author} and published in {self.year}')