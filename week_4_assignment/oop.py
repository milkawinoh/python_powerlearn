class Person:
    """
    A class representing a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        gender (str): The gender of the person ('male', 'female', etc.).
    """

    def __init__(self, name, age, gender):
        """
        Initializes a new Person object with the given attributes.

        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
            gender (str): The gender of the person ('male', 'female', etc.).
        """
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        """
        Prints a message introducing the person with their name, age, and gender.
        """
        print(f"Hello, I am {self.name}. I am {self.age} years old and {self.gender}.")

person1 = Person("milka", 24, "female")
person1.introduce()