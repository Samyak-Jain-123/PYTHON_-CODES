#Program 1 (Name / Age)
a= input("Enter your Name=")
b= int(input("Enter your Age="))

print (f"Hello {a}, your age is {b}")



#Program 2 (Operators)
a= float(input("Enter your first number:")) 
b= float(input("Enter your second number:"))

print ("Average of the above two given numbers is", (a+b)/2) 

add=a+b
print ("Addition of the above two given numbers is",add) 

diff=a-b
print ("Difference of the above two given numbers is" ,diff)

mul=a*b
print("Multiplication of the above two given numbers is",mul)

div=a/b
print ("Division of the above two given numbers is",div)

power = a**b
print ("Power of the above two given numbers is", power)

modu= a%b
print ("Remainder when a is divided by b is =", modu)



#Program 3 (Average)
a= float(input("Enter your first number:")) 
b= float(input("Enter your second number:")) 
c= float(input ("Enter your third number:"))

print ("Average of the above given numbers is =", (a+b+c)/3)



#Program 4 (Type casting)
a= (input ("Enter an integer=" ))
print (a)
print(type(a))

a=int(a)
print (a)
print(type(a))

a=float (a)
print (a)
print (type(a) )



#Program 5 (Integer type)
x=10+3*2**2
print (x)
print (type(x))



#Program 6 (Swapping numbers)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a
print("After swapping:")
print("First number =", a)
print("Second number =", b)



#Program 7 (Celsius --> Fahrenheit)
a=float(input("Enter value in Celsius="))
b= (a*9/5)+32

print("Your value in Fahrenheit is",b)



#Program 8 (Area of circle)
r= float(input("Enter the radius of your circle="))

a= 3.14*r**2

print(f"Area of the circle with radius {r} is {a}")



#Program 9 (Simple interest)
a = float(input("Enter your principal amount= "))
b = float(input("Enter your rate of interest= "))
c = float(input("Enter your time period (in years)= "))

si = a*b*c/100
print("Simple interest=",si)



#Program 10 (Integer and Fractional part)                                       
a = float(input("Enter a decimal number: "))

x = int(a)
y = float(a-x)

print("Integer part =", x)
print("Fractional part =", y)
print("Fractional part rounded to 3 decimals =", f"{y:.3f}")







