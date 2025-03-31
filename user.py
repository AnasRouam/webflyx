class User:
    def __init__(self, name, last_name, age, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email

    def __repr__(self):
        print(f'User("{self.name}", "{self.last_name}", "{self.age}", "{self.email}")')

    def __str__(self):
        print(f'This User is called {self.name} {self.last_name}. He/She is {self.age}.')