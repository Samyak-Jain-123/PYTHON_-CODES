#Conditional Statements    (if-elif-else)
a = int(input("Enter your age: "))

if(a>=21):
    print("You can Vote")
    print("You can become a MLA")

elif(a>=18):
    print("You can Vote")
    print("You can't become a MLA")

else: 
    print("You can't Vote")
    print("You can't become a MLA")


# There can be multiple "if" and "elif" statements, but only one "else" in one chain.
# "if-elif-else" always starts with an "if" statement
# Separate "if" statements are checked independently.
# In an if-elif-else chain, Python stops after the first true condition.


b = input("What is the colour at traffic signal: ").lower()

if (b == "red"):
     print ("stop")

elif(b == "green"):
    print ("go" )

elif(b == "yellow"):
    print ("look")

else:
    print("Light is broken")



#Nesting
a = int(input("Enter your age: "))

if (a >= 18):
    if (a >= 80):
        print ("Cannot drive")
    else:
        print ("can drive")
        
else:
    print ("cannot drive")
