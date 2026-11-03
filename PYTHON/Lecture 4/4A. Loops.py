#LOOPS --> used to repeat instructions.  
#It is of two types:    1. 'while' loop   2. 'for' loop

#Remember - INFINITE LOOPS ARE DANGEROUS



#1. WHILE LOOP (repeat while a condition is True)

# Break ---> used to terminate the loop when encountered.
# Continue ---> terminates execution in the current iteration & continues execution of the loop with the next iteration.


# Example 1 - print HELLO 5 times
i = 1      
while i <= 5:                    
    print("HELLO",i)                    
    i += 1


# Example 2 - print 5 to 1
i = 5
while i > 0:
    print(i)
    i -= 1


# Example 3 - search for a number x in a list (Easy)
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]
x = int(input("Enter the number u want to find: "))

i = 0
while i < len(l):
    if l[i] == x:
        print("FOUND at idx", i)
    i += 1
'OR'

a=0
for i in l:
    if(i == x):
        print("number found at index",a)
    a += 1


# Example 4 -  Break for multiple of 4
i = 1
while i <= 10:
    if(i % 4 == 0):
        break
    print(i)
    i += 1
print("This loop is stopped at a multiple of 4")


# Example 5 -  Continue for multiples of 3
i = 0
while(i < 10):
    i += 1
    if(i % 3 == 0):
        continue
    print(i)
print("This loop skips the multiple of 3")



#FOR LOOP (iterate over a sequence i.e a list, string, or range)

# range()--> The range function returns a sequence of numbers, starting from 0 by default, 
#            and increments by 1 (by default), and stops before a specified end value

# pass ---> It is a null statement that does nothing. It is used as a placeholder for future code.


# Example 1 - Sum and Factorial of first n numbers
x= int(input("Enter the number: "))

i=0
add = 0
fac = 1
while i<x:
    i+=1
    add = add + i
    fac = fac * i
    
print("Total SUM= ", add)
print("Factorial= ", fac)
'OR'

add = 0
fac = 1
for i in range(1,x+1):
     add = add + i
     fac = fac * i

print("Total SUM= ", add)
print("Factorial= ", fac)


# Example 2 - Looping over a string
word ="Good"
for i in word:
    print(i)


# Example 3 - Check if char 'i' exists in word
word="Prime"
if 'i' in word:
    print("letter exists")
else:
    print("letter doesn't exist")


# Example 4 - Count number of i's in the word
word = "Artificial Intelligence"
l = 0
for a in word:
    if a == 'i' or a=='I':
        l += 1

print("letter 'i' occurs",l,"times.")


# Example 5 - Nested Loops
for i in range(1, 3):
    for j in range(1, 3):
        print(f"({i}, {j})")
# output: (1, 2) (1, 2) (2, 1) (2, 2)

