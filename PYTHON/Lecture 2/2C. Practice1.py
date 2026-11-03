#Question 1 (Atm Machine)
b = 10000          # Initial balance

print("OPTIONS:")
print("Check balance    -1")
print("Withdraw Money   -2")
print("Deposit Money    -3")

a =  int(input("Enter your choice from the given above options (1/2/3): "))

if (a == 1):
    print ("Your current balance is:", b)


elif(a == 2):
    x = int(input("Enter the amount to be withdrawn: "))
    
    if (x<=b):
        b = b-x 
        print("Successfully withdrawn")
        print("Your current Balance is:", b )
        
    else:
        print("Insufficient Balance, please try again")


elif(a == 3):
    y=int(input("Enter the amount to be deposited:"))

    b=b+y
    print("Amount Updated")
    print("Your current Balance is:", b )


else:
    print("Invalid option, please try again")



#Question 2 (Area of the Shape)
print("OPTIONS:")
print("Triangle          -1")
print("Square            -2")
print("Rectangle         -3")

a = int(input("Choose the shape from the given above options whose area need to be calculated(1/2/3): "))

if (a == 1):
    x=float(input("Enter the height of the triangle: "))
    y=float(input("Enter the base of the triangle: "))
    z=(x*y)/2
    print("Area of the triangle: ", z)


elif(a == 2): 
    x=float(input("Enter the side length of the square: "))
    z = x*x
    print("Area of the square: ",z)
 

elif (a == 3):
    x=float(input("Enter the length of the rectangle: "))
    y=float(input("Enter the breadth of the rectangle: "))
    z=x*y
    print("Area of the rectangle: ", z)


else: 
    print("Data Not Available")



#Question 3 (Simple Calculator)
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

print("OPTIONS:")
print("Addition          -1")
print("Subtraction       -2")
print("Multiplication    -3")
print("Division          -4")

a =  int(input("Enter your choice from the given above options (1/2/3/4): "))

if a==1:
    print(x+y)

elif a==2:
    print(x-y)

elif a==3:
    print(x*y)

elif a==4:
    print(x/y)

else:
    print("Invalid option")

