#INTRODUCTION
print ("Welcome back Captain. ")
print ("All systems are ready.")

print ("Welcome back Captain.", "All systems are ready.")



#DATA TYPES
name = "Sam"
print (name)
print (type(name))          # <class 'str'>

age = 18
print (age)
print (type(age))           # <class 'int'>

marks = 93.2
print(marks)
print (type (marks))        # <class 'float'>

job = None 
print (job)
print (type(job))           # <class 'NoneType'>

alive = True 
print (alive)
print (type (alive))        # <class 'bool'>



#1. Type conversion (automatically done by Python)
a = 5
b = 3.0
c = (a + b)                 # Python automatically converts the integer to float during addition
print(c)
print(type(c))              # <class 'float'>


#2. Type casting (done manually by the programmer)
x = 10                      
y = float(x)                
z = str(x)   

print(x)
print(type(x))              # <class 'int'>

print(y)
print(type(y))              # <class 'float'>

print(z)
print(type(z))              # <class 'str'>



#OPERATORS:
#1. Arithmetic Operators
a = 6
b = 2
add = a + b
print("Addition:", add)

diff = a - b
print("Subtraction:", diff)

mul = a * b
print("Multiplication:", mul)

div = a / b
print("Division:", div)     # 3.0, answer is always float
print(type(div))            # <class 'float'>

power = a ** b
print("Power:", power)
print("gfh")
modu = a % b
print("Modulo:", modu)

# In Python, the remainder has the same sign as the divisor
print("5%-2:" ,  5%-2)      # -1
print("-5%2"  , -5% 2)      #  1
print("-5%-2:", -5%-2)      # -1


a=5
b=2
int_div = a//b                  
print(int_div)              # 2
print(type(int_div))        # <class 'int'>

# // = Integer division (division + floor)

a=5.0
b=2
int_div = a//b                  
print(int_div)              # 2.0
print(type(int_div))        # <class 'float'>


# String & integer values can operate together with *
a = "@"
print (4*a)   

# String & String can operate with +
a = "J"
b = "K"
print ((a+b)*4)



#2. Relational Operators
a = 10
b = 20
print("a == b:", a == b)    # False

print("a != b:", a != b)    # True

print("a > b:", a > b)      # False

print("a < b:", a < b)      # True

print("a >= b:", a >= b)    # False

print("a <= b:", a <= b)    # True



#3. Assignment Operators
x = 10
print("x =", x)             # 10

x += 5                      # equivalent to x = x + 5
print("x += 5 ->", x)       # 15

x -= 3                      # equivalent to x = x - 3
print("x -= 3 ->", x)       # 12

x *= 2                      # equivalent to x = x * 2
print("x *= 2 ->", x)       # 24

x /= 4                      # equivalent to x = x / 4
print("x /= 4 ->", x)       # 6.0

x %= 4                      # equivalent to x = x % 4
print("x %= 4 ->", x)       # 2.0

x **= 3                     # equivalent to x = x ** 3
print("x **= 3 ->", x)      # 8.0



#4. Logical Operators 
a=5
b=2
print("OR:",a>b or a==b)    # True
 
print("AND:",a>b and a==b)  # False

print("NOT:",not(a>b))      # False



#5. Bitwise Operators
a=10
b=3
print("AND:", a&b)          # 2

print("OR:", a|b)           # 11
 
print("XOR:", a^b)          # 9

print("NOT:", ~a , ~b)      # -11 & -4      [   ~x = -(x+1)    ]

print("LEFT SHIFT:", a<<b)  #80             [ x<<y = x * 2**y  ]

print("RIGHT SHIFT:", a>>b) #1              [ x>>y = x // 2**y ]



