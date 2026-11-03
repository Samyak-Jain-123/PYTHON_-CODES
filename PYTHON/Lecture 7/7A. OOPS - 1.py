# OOP (OBJECT ORIENTED PROGRAMMING)

# Class & Object ---> A class is a blueprint, and an object is an instance of that blueprint

# 1. Creating class
class Student:
    name = "Karan"

# 2. Creating object/instance of that class
s1 = Student()
print(s1)                                       # <__main__.Student object at ...>
print(s1.name)                                  # Karan



# '__init__' Function (Constructor)
# All classes have a function called __init__(), which is always executed when the object is being initiated

# 1. Default Constructors - A constructor with no parameters except 'self'
# 2. Parameterized Constructors - Takes parameters to initialize values uniquely for each object

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
# or in simple words, 'self' refers to the current object that is being created


# 1. Creating class 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding a new student...")

# 2. Creating object
s1 = Student("Karan1",93)                          
print(s1)                                       # <__main__.Student object at ...>
print(s1.name)                                  # Karan1
print(s1.marks)                                 # 93

s2 = Student("Karan2",99)                          
print(s2)                                       # <__main__.Student object at ...>
print(s2.name)                                  # Karan2
print(s2.marks)                                 # 99



# Attributes ---> They are variables that belong to a class or an object. They store data/state of the object

# 1. Class Attributes
# • Belong to the class itself, shared by all objects
# • Defined outside any method in the class


# 2. Instance Attributes
# • Belong individually to each object
# • Defined inside '__init__' method using self


class Student:
    college = "ABC college"                     # class attribute
    def __init__ (self, name):             
        self.name = name                        # instance attributes            

s1 = Student("Rahul")
print(s1.college)
print(s1. name)
print(Student.college)                          # class attribute can also be accessed with class name



# Methods ---> They are functions defined inside a class, representing the behaviour or actions of an object.

# 1. Instance Methods
# • Take 'self' as the first argument
# • Can access both instance attributes and class attributes


# 2. Class Methods
# • Use '@classmethod' decorator
# • Take 'cls' (class) as first argument
# • Used to work with class-level data


# 3. Static Methods
# • Use '@staticmethod' decorator
# • Do not take 'self' or 'cls'
# • Behave like normal functions but belong to the class for logical grouping



class Student:
    school_name = "ABC School"

    # Constructor
    def __init__(self, name):
        self.name = name

    # Instance method
    def greet(self):                            
        print(f"Welcome Back Captian {self.name}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def add(a, b):
        return a + b


s1 = Student("Samyak")
#1
print(s1.name)
s1.greet()

s1. name = "Ironman"
print(s1.name)
s1. greet()

#2
print(s1.school_name)
s1.change_school("XYZ School")
print(s1.school_name)

s2 = Student("Samyak")
print(s2.school_name)

#3
print(s1.add(3,5))
print(Student.add(3,5))



#OOP Pillars
# 1. Abstraction ---> Hiding the implementation (unnecessary) details of a class and only showing the essential features to the user.
# 2. Encapsulation ---> Wrapping data and functions into a single unit (object)




