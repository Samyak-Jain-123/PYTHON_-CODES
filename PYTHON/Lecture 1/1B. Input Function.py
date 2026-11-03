# INPUT function
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Welcome", name)
print("Your age is", age)

print(type(name))                       # Result for input() is always a str
print(type(age))                    



# Calculator
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))

print("The sum of the above two numbers is:", a + b)
print("The average of the above two numbers is:", (a + b) / 2)



# Area of Square Calculator
a = float(input("The side of the square: "))

print("The area of the square:", a * a)




