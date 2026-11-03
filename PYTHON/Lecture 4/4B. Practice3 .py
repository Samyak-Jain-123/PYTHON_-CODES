# Question 1 [Searching for a number (Only showing result that is in one line)]        ------ EXPERT 3
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]
x = int(input("Enter the number u want to find: "))

i = 0
l=[]
found = False
while i < len(nums):
    if nums[i] == x:
        l.append(i)
        
        found = True
    i += 1

if not found:
    print("This number is not available in the list")

else:
    print("This number is found at ind:",l)
'OR'

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]       
x = int(input("Enter the number u want to find: "))

l=[]
j=False
for i in range(len(nums)):
  if(nums[i]==x):
      l.append(i)
      j=True
if j:
 print("This number is found at ind:",l)

else:
    print("This number is not available in the list")



#Question 2 (Position of letter "s" in a word)                                         ------ EXPERT 4
word= input("Enter a word:")

j=0
k=False
l=[]
for i in word:
 if i=='s':
    l.append(j)
    k=True
 j+=1

if  k:
    print("Letter 's' exists at indexes:",l)
else:
  print("Letter doesn't exist")



#Question 3 (Total number of digits in a number)                                       ------ EXPERT 5
a= int(input("Enter a number:"))

i=1
while a>=10:
    a=a//10
    i+=1
print("Total Number of digits:",i)



#Question 4 (Number obtained after reversing its digits)                               ------ EXPERT 6
a= int(input("Enter a number:"))

b=0
while a>0:
    c=a%10
    a=a//10
    b=b*10+c
print("Number after reversing its digits:",b)



#Question 5 (Word obtained after reversing its letters)                                ------ EXPERT 7
a=input("Enter a str:")
l=len(a)
n=0
c=""
while n<l:
    b=a[n]
    c=b+c
    n+=1
print("After reversing alphabet:",c)



#Question 6 (Word Palindrome in 2 AND 1 LINES)                                           ------ EXPERT 8
a = input("Enter a str:").lower()                                                                        
print("Palindrome") if (a==a[::-1]) else print("Not Palindrome")

"OR"
print("Palindrome" if ( a := input ("Enter a str:").lower() ) == a[::-1] else "Not Palindrome")  



#Question 7 (List of Odd and Even Numbers)
x=[]
y=[]
for a in range(1,51):
    if a %2==0:
        x.append(a)

    if a %2!=0:
        y.append(a)

print("even", x)
print("odd", y)





