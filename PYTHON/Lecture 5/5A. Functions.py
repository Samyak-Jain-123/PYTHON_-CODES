#FUNCTIONS
# Functions are blocks of reusable code that perform a specific task. They make our code organized, readable, and easier to maintain.


#User-Defined Functions 
#1. Function Definition ---> We use the 'def' keyword to define our function
def func_name (a, b):               # a & b are parameters 
    print(a + b)

#2. Function Calling
func_name (3,4)                     # 3 & 4 are arguments
print(func_name (3,4))              # prints 7, then returns None



#Built-in Functions
print("Hello","Sam",   "Good")      # sep = " " | # end = \n

print("Hello","Sam", sep= "$$" ,end= " ")            
print("Good")



# Default Parameters
# We can assign default values to function parameters so that if the caller doesn’t provide that argument, Python uses the default values

def add(b, a = 1):                  # default val of a is 1
    return a + b
print(add(5))                       # output: 6



#Recursion ---> It is like a Loop where a function calls itself repeatedly

#Example 1 - Prints n to 1 backwards
def show(n):
    if(n == 0):                     # Here 'if' statement is called 'base case'            
        return                      # Command Return
    print(n)
    show(n-1)
    print("END", n)
show(3)

# Example 2 - Sum and Factorial of first n numbers
def fact(n):
    if(n == 0 or n == 1):
        return 1 
    return n * fact(n-1)
    
def addi(n):
    if n == 0:
        return 0
    return n + addi(n-1)
    
print(fact(4))
print(addi(4))



