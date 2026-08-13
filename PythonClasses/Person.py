class Person:
    def __init__(self, name, age, dob, gender, address, phone_number, email):
        self.name = name
        self.age = age
        self.dob = dob
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def walk(self):
        return f"{self.name} is walking."

    def talk(self):
        return f"{self.name} is talking."

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def update_name(self, new_name):
        self.name = new_name
        return f"Name updated to {self.name}."

    def update_age(self, new_age):
        self.age = new_age
        return f"Age updated to {self.age}."

    def address_update(self, new_address):
        self.address = new_address
        return f"Address updated to {self.address}."

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        return f"Phone number updated to {self.phone_number}."

    def update_email(self, new_email):
        self.email = new_email
        return f"Email updated to {self.email}."

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "dob": self.dob,
            "gender": self.gender,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email
        }


duyu = Person("Duyu", 19, "2010-26-10", "Male", "123 Main St", "123-456-7890", "duyu@example.com")

print(duyu.get_info())  # Output: {'name': 'Duyu', 'age': 19, 'dob': '2010-26-10', 'gender': 'Male', 'address': '123 Main St', 'phone_number': '123-456-7890', 'email': 'duyu@example.com'}

duyu.update_name("Duyu Updated")
duyu.update_age(18)
duyu.address_update("456 Elm St")
duyu.update_phone_number("098-765-4321")
duyu.update_email("duyu.updated@example.com")

print(duyu.get_info())  # Output: {'name': 'Duyu Updated', 'age': 18, 'dob': '2010-26-10', 'gender': 'Male', 'address': '456 Elm St', 'phone_number': '098-765-4321', 'email': '  


vishal = Person("Vishal", 20, "2003-15-05", "Male", "789 Oak St", "987-654-3210", "vishal@example.com")

print(vishal.get_info())  # Output: {'name': 'Vishal', 'age': 20, 'dob': '2003-15-05', 'gender': 'Male', 'address': '789 Oak St', 'phone_number': '987-654-3210', 'email': 'vishal@example.com'}
vishal.update_name("Vishal Updated")
print("Vishal Info:", vishal.get_info())  # Output: {'name': 'Vishal Updated', 'age': 20, 'dob': '2003-15-05', 'gender': 'Male', 'address': '789 Oak St', 'phone_number': '987-654-3210', 'email': 'vishal.updated@example.com'}