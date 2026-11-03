#1. Calculator 
def calculator():
    print("Welocome to Calculator")
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    op= input("Enter your operator: ")

    #1
    if op == "+":
        return(a+b)

    elif op == "-":
        return(a-b)

    elif op == "*":
        return(a*b)

    elif op == "/":
        return(a/b)
    
    elif op == "%":
        return(a%b)
    
    elif op == "//":
        return(a//b)
    
    elif op == "**":
        return(a**b)
    
    elif op == "√":
        return(a**(1/b))
    
    #2
    elif op == ">":
        return(a>b)
    
    elif op == "<":
        return(a<b)
    
    elif op == "==":
        return(a==b)
    
    #3
    elif op == "&":
        return(a&b)
    
    elif op == "|":
        return(a|b)
    
    elif op == "^":
        return(a^b)
    
    elif op == ">>":                                     
        return(a>>b)
    
    elif op == "<<":                                     
        return(a<<b)
    
    else:
        return(None)



#2. Prime Number
def is_prime():
   while True:
     print("Enter a number to check whether it is prime or not")
     n = int(input("Enter a input: "))
    
     if n==1 or n==0:
         print("It is neither prime nor composite")
         return None
     
     elif n<0:
         print("Can't say about negative numbers")
         return None
 
     else:
            a = int(n**0.5) + 1
            b = True
            for i in range (2,a):
                if n%i==0:
                    b = False
            return b

   print("End of Loop")



#3. Factorial
def factorial():
    x= int(input("Enter the number whose factorial is needed: "))

    if x<0:
        print("Can't say about negative numbers")
        return(None)

    else:
        i=0
        fac = 1
        while i<x:
            i+=1
            fac = fac * i
    
    return(fac)



#4. Simple interest
def si():
    print("Welcome! Calculate the simple interset")
    a = float(input("Enter your principal amount= "))
    b = float(input("Enter your rate of interest= "))
    c = float(input("Enter your time period (in years)= "))

    si = a*b*c/100
    return(si)



#5. Perimeter & Area
def p_a():
    print("OPTIONS:")
    print("Triangle          -1")
    print("Square            -2")
    print("Rectangle         -3")
    print("Circle            -4")

    a = int(input("Choose the shape from the given above options (1/2/3/4): "))

    print("OPTIONS:")
    print("PERIMETER         -1")
    print("AREA              -2")

    b = int(input("Choose from given above options (1/2): "))

    if b == 1:
        if (a == 1):
            w=float(input("Enter 1st side length of the triangle: "))    
            x=float(input("Enter 2nd side length of the triangle: "))
            y=float(input("Enter 3rd side length of the triangle: "))
            z=(x+y+w)
            return(z)
        elif(a == 2): 
            x=float(input("Enter the side length of the square: "))
            z = 4*x
            return(z)
        elif (a == 3):
            x=float(input("Enter the length of the rectangle: "))
            y=float(input("Enter the breadth of the rectangle: "))
            z=2*(x+y)
            return(z)
        elif (a==4):
            x=float(input("Enter the radius of circle: "))
            z = 2*22/7*x
            return(z)
        else: 
            print("Data Not Available")
            return(None)
        

    if b == 2:
        if (a == 1):    
            x=float(input("Enter the height of the triangle: "))
            y=float(input("Enter the base of the triangle: "))
            z=(x*y)/2
            return(z)
        elif(a == 2): 
            x=float(input("Enter the side length of the square: "))
            z = x*x
            return(z)
        elif (a == 3):
            x=float(input("Enter the length of the rectangle: "))
            y=float(input("Enter the breadth of the rectangle: "))
            z=x*y
            return(z)
        elif (a==4):
            x=float(input("Enter the radius of circle: "))
            z = 22/7*x*x
            return(z)
        else: 
            print("Data Not Available")
            return(None)






