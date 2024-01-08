#Create a Person class with attributes like name, age, and address. Include methods to update and display the person's information.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_information(self, new_name=None, new_age=None, new_address=None):
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        if new_address:
            self.address = new_address

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


person1 = Person(name="Midhun p", age=21, address="Mlappuram Kerala")


print("Information:")
person1.display_information()


person1.update_information(new_name="Midhun p", new_age=22, new_address="Kochi Kerala")


print("\nUpdated Information:")
person1.display_information()
