from dogClass import Dog


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
