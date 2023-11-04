# Define the Person class with encapsulation for the age attribute
class Person:
    def __init__(self, name, age, gender, profession):
        self.name = name
        self.__age = age  # Private attribute
        self.gender = gender
        self.profession = profession

    # Getter method for age attribute
    def get_age(self):
        return self.__age

    # Setter method for age attribute
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

    # Method to print person details
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.__age}, Gender: {self.gender}, Profession: {self.profession}")

# Define the Student subclass that inherits from Person
class Student(Person):
    def __init__(self, name, age, gender, profession, student_id):
        super().__init__(name, age, gender, profession)  # Call the constructor of the base class
        self.student_id = student_id  # Additional attribute for Student

    # Override the print_details method to include Student-specific details
    def print_details(self):
        super().print_details()  # Call the print_details method of the base class
        print(f"Student ID: {self.student_id}")

# Create instances of Person and Student
person1 = Person("Alex", 29, "Female", "Solicitor")
person2 = Person("Gary", 37, "Male", "Founder")
student1 = Student("Ailish", 28, "Female", "Brain Stuff", 12345)
student2 = Student("Sarah", 31, "Female", "Law Studies", 98765)

# Create a function to demonstrate polymorphism
def print_person_details(person):
    person.print_details()  # Call the print_details method of the object

# Call the print_person_details function with instances of Person and Student
print_person_details(person1)  # Calls Person's print_details
print_person_details(person2)  # Calls Person's print_details
print_person_details(student1)  # Calls Student's print_details (polymorphism)
print_person_details(student2)  # Calls Student's print_details (polymorphism)