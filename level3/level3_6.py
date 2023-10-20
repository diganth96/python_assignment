class Grandparent:
    def __init__(self, name):
        self.name = name

    def grandparent_method(self):
        print(f"{self.name} is a grandparent.")

class Parent(Grandparent):
    def parent_method(self):
        print(f"{self.name} is a parent.")

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

class Pet(Dog, Cat):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"{self.name} is a {self.species}.")

class Child(Parent, Pet):
    def __init__(self, name, species, toy):
        Parent.__init__(self, name)
        Pet.__init__(self, name, species)
        self.toy = toy

    def child_method(self):
        print(f"{self.name} has a {self.toy}.")

# Example usage
child = Child("Alice", "Dog", "Frisbee")
child.grandparent_method()  # Calls the method from Grandparent class.
child.parent_method()  # Calls the method from Parent class.
child.introduce()  # Calls the method from Pet class.
child.child_method()  # Calls the method from Child class.
print(child.speak())  # Calls the speak method from the Dog class (first base class).
