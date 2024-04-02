# Create a Python class named Person.
class Person:
    def __init__(self, name, age, gender):
        # The Person class should have the following attributes:name,age and gender
        self.name = name
        self.age = age
        self.gender = gender

    # Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
    def display_info(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am {self.gender}.")


# Create an instance of the Person class and call the introduce method to display the person's information.
person1 = Person("Sally", 37, "Female")
person1.display_info()
