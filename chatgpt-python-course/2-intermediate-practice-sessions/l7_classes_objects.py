class Person: # Creating a Class
    def __init__(self, name, age, gender, profession):
        self.name = name
        self.age = age
        self.gender = gender
        self.profession = profession
    
    def print_details(self): # Set what printing looks like
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Profession: {self.profession}")
    
        class Student(Person):
            def __init__(self, name, age, gender, profession, student_id):
                super().__init__(name, age, gender, profession)
                self.student_id = student_id
    
            def print_details(self):
                super().print_details()
                print(f"Student ID: {self.student_id}")

person1 = Person("Alex", 29, "Female", "Solicitor")
person2 = Person("Gary", 37, "Male", "Founder")

person1.print_details()  # Output: Name: Alex, Age: 29, Gender: Female, Profession: Solicitor
person2.print_details()  # Output: Name: Gary, Age: 37, Gender: Male, Profession: Founder

