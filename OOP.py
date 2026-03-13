class Dog:
    species = 'Canis Familiaris'

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f'Dog({self.name}, {self.breed}, age {self.age})'

    def __repr__(self):
        return f"Dog('{self.name}', '{self.breed}', {self.age})"

    def bark(self):
        return f'{self.name} says: Woof!'

    def birthday(self):
        self.age += 1
        return f'{self.name} is now {self.age}'

    @classmethod
    def from_string(cls, dog_string):
        name, breed, age = dog_string.split(',')
        return cls(name.strip(), breed.strip(), int(age))

    @staticmethod
    def is_adult(age):
        return age >= 2

return f"{self.__class__.__name__}({self.name})"


