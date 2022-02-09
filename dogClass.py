# each instance created from the Gog class will store a name and an age
# and we will give each dog the ability to sit () and roll_over():
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """instialize name and attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """'simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over in response to command"""
        print(f"{self.name} rolled over!")
