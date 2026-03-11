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

    # --------- Create Object ----------
dog1 = Dog("Buddy", "Labrador", 3)

# --------- Call Methods ----------
print(dog1)
print(dog1.bark())
print(dog1.birthday())

# Using class method
dog2 = Dog.from_string("Max, German Shepherd, 2")
print(dog2)

# Using static method
print("Is Adult:", Dog.is_adult(dog2.age))
