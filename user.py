class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        print(f'User({self.name}, {self.last_name}, {self.age})')

    def __str__(self):
        print(f'This User is called {self.name} {self.last_name}. He/She is {self.age}')