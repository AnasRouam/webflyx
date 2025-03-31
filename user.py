class User:
    def __init__(self, name, last_name, age, email, rented_books_ids):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.rented_books_ids = rented_books_ids

    def __repr__(self):
        return f'User("{self.name}", "{self.last_name}", "{self.age}", "{self.email}")'

    def __str__(self):
        return f'This User is called {self.name} {self.last_name}. He/She is {self.age}. You can reach him via email at {self.email}'