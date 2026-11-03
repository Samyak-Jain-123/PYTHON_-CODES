#Program 1 (Palindrome)
a = input("Enter a str: ").lower()                                                                        
print("Palindrome") if (a==a[::-1]) else print("Not Palindrome")
"OR"
print("Palindrome" if ( a := input ("Enter a str: ").lower() ) == a[::-1] else "Not Palindrome")  



#Program 2 (Average of List)
l1 = [0,1,2,3,4,5,6,7,8,9,10]
print( sum(l1) / len(l1) )



#Program 3 (Merge lists)
l1 = list(map(int, input("Enter the elements of first list (space-separated): ").split()))
l2 = list(map(int, input("Enter the elements of second list (space-separated): ").split()))

l3 = l1+l2
l3.sort()
print(l3)



#Program 4 (Tuple of Even & Odd)
t = (0,1,2,3,4,5,6,7,8,9,10)
x=[]
y=[]

for i in t:
    if i%2==0:
        x.append(i)
    else:
        y.append(i)

x=tuple(x)
y=tuple(y)

print(x,y)



#Program 5 (Student Dictionary)
d = {
    "Ram"     :43,
    "Shyam"   :24,
    "Om"      :45,
    "Rahul"   :36,
    "Harshit" :21
}

print("OPTIONS: ")
print("       Add a student                     -A")
print("       Update marks                      -B")
print("    Search for a student                 -C")
print(" Display all students and marks          -D")

a =  input("Enter your choice from the given above options (1/2/3/4): ").upper()

if   a == 'A':
    name = input("Enter the new student name: ")
    marks = int(input("Enter his/her marks: "))

    d.update({name:marks})

elif a == 'B':
    name = input("Enter the student name whose marks is getting updated: ")
    marks = int(input("Enter his/her new marks: "))

    d.update({name:marks})

elif a == 'C':
    name = input("Enter the student name whose marks is getting searched: ")
    print(f"{name} : {d[name]}")

elif a == 'D':
    print(d) 



#Program 6 (Length Dictionary)
words = ["apple","banana","kiwi","cherry","mango"]
d={}

for i in words:
    j = len(i)
    d[i]=j

print(d)



#Program 7 (Space Detection)
a = input("Enter a str: ")
b = a.count(" ")
print(f"Total number of times you have pressed spacebar in your entire string is {b}")



#Program 8 (No common elements)
l1 = list(map(int, input("Enter the elements of first list (space-separated): ").split()))
l2 = list(map(int, input("Enter the elements of second list (space-separated): ").split()))

s1=set(l1)
s2=set(l2)
s3= s1.intersection(s2)

if len(s3) == 0:
    print("There are no common elements in the given two lists")
else:
    print("Common elements in the given two lists are: ",s3)



#Program 9 (Repeating elements)
l1 = list(map(int, input("Enter the elements of first list (space-separated): ").split()))

s1 = set()
s2 = set()

for i in l1:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)

print("Elements appearing more than once:", s2)



#Program 10 (Unique Characters)                                       
a = input("Enter a str: ")
l=[]

for i in a:
    if i == " ":
        pass
    elif i not in l:
        l.append(i)
    
print("UNIQUE CHARACTERS: ",l)
print("COUNT OF UNIQUE CHARACTERS: ", len(l))







