x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))


#1. Function with No Parameters
def add():
    print(x+y)
add()

def mul():
    print(x*y)
mul()


#2. Function with Parameters
def addi(a,b):
    print(a+b)
addi(x, y)

def mult(a,b):
    print(a*b)
mult(x, y)


#3. Function with No Parameters but return a value
def addit():
    return x+y
print(addit())

def multi():
    return x*y
print(multi())


#4. Function with Parameters and return a value
def addition(a,b):
    return a+b
print(addition(x,y))

def multiplication(a,b):
    return a*b
print(multiplication(x,y))



x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=input("Enter a string:")


#Question 1 (MAX function)
def maxi(a,b):
    if a > b:
        return a
    elif b > a:
        return b 
    else:
        return "Both are equal"


#Question 2 (EVEN OR ODD function)
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


#Question 3 (LIST SUM function)
def list_sum(n):
    a = 0
    for i in n:
        a += i
    return a 


#Question 4 (COUNT VOWEL function)
def count_vowels(n):
    vowels = "aeiou"
    a = 0
    for i in n.lower():
        if i in vowels:
            a += 1
    return a 


#Question 5 (Palindrome function)
def is_palindrome(n):
    n = n.lower()
    return n == n[::-1]


#Question 6 (Fibonacci function)
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        a = 0
        b = 1
        l=[0,1]
        i = 2
        while i<n:
            a, b = b, a + b
            l.append(b)
            i+=1
        return l


#1
print(maxi(x,y))
#2
print(even_or_odd(x))
print(even_or_odd(y))
#3
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
print(list_sum(l))
#4
print(count_vowels(z))
#5
print(is_palindrome(z))
#6
print(fibonacci(x))
print(fibonacci(y))

