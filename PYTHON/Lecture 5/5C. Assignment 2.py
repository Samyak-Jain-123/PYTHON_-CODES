#Program 1 (Salary/ Tax rate)
a= int(input("Enter your salary amount:"))

if a<=30000:
    b= 5

elif a<=70000:
    b= 15

elif a>70000:
    b=25

print(f"Final tax rate on your input salary: {b} %")
print("Final tax amount:", a*b/100)



#Program 2 (Even Number between x & y)
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

def fxn(a,b):
    l=[]
    for i in range (a,b+1):
        if i%2 == 0:
            l.append(i)

    return(l)    

print(f"Even numbers between your two numbers are {fxn(x,y)}")



#Program 3 (Print digits of a Number)
x= int(input("Enter a number:"))

def digit(a):
 l=[]
 while a>0:
    i=a%10
    a=a//10
    l.insert(0,i)
 print(l)

digit(x)



#Program 4 (Total number of digits in a number)                                      
x= int(input("Enter a number:"))

def ndigit(a):
    i=0
    if a == 0:
        print("Total Number of digits:",1) 

    else:
        while a>0:
            a=a//10
            i+=1
        print("Total Number of digits:",i)
print(ndigit(x))



#Program 5 (Sum of digits)
x= int(input("Enter a number:"))

def digit(a):
 
 m=[]
 while a>0:
    i=a%10
    a=a//10
    m.append(i)
 return(sum(m))

print(f"Sum of its digits is {digit(x)}")



#Program 6 (Number divisible by both 3 & 5)
l=[]
for i in range (1,101):
   if i % 15==0:
      l.append(i)
print("Number divisible by both 3 & 5 are",l)



#Program 7 (Positive or Negative)
while True:
    print("Enter a number to tell whether it is positive or negative. To exit the program enter -->  Q")
    a = input("Enter a input: ")

    if a == 'Q':
      break

    a=int(a)
    if a>0 :
        print("Number is positive")
    elif a<0 :
        print("Number is negative")
    elif a==0:
        print("This number is neither positive nor negative")

print("End of Loop")



#Program 8 (Simple Calculator using functions)
def calculator(a,b,op):
    if op == "+":
        return(a+b)

    elif op == "-":
        return(a-b)

    elif op == "*":
        return(a*b)

    elif op == "/":
        return(a/b)
    
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z= input("Enter your operator: ")

l= calculator(x,y,z)
print("Output =", l)

'OR'
def addit(a,b):
    return(a+b)

def subtr(a,b):
    return(a-b)

def multi(a,b):
    return(a*b)

def divis(a,b):
    return(a/b)


x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))

print("OPTIONS:")
print("Addition          -1")
print("Subtraction       -2")
print("Multiplication    -3")
print("Division          -4")

a =  int(input("Enter your choice from the given above options (1/2/3/4): "))

if a==1:
    print(addit(x,y))

if a==2:
    print(subtr(x,y))

if a==3:
    print(multi(x,y))

if a==4:
    print(divis(x,y))




#Program 9 (Prime Numbers)
def is_prime():
   while True:
     print("Enter a number to check whether it is prime or not. To exit the program enter -->  Q ")
     n = input("Enter a input: ")
    
     if n == 'Q':
         break

     n=int(n)
     if n==1 or n==0:
         print("It is neither prime nor composite")
     elif n<0:
         print("Can't say about negative numbers") 
     else:
            a = int(n**0.5) + 1
            b = True
            for i in range (2,a):
                if n%i==0:
                    b = False
            print(f"Prime Number: {b}")

   print("End of Loop")

is_prime()



#Program 10 (Number Guessing Game)
import random
Srt = random.randint(0, 100)
# Srt = 48

while True:
    print("Try to guess the Secret number that is between 0-100")

    a = int(input("Enter the guessing number: "))

    if a>Srt :
        print("Too High, Try again")
    elif a<Srt :
        print("Too Low, Try again")
    elif a==Srt:
        print("Congrats! You guessed it correctly. Here is your reward: 🫥")
        break
    
print("End of Loop")

