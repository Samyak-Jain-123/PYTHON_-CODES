# File Input & Output
# Python can be used to perform operations on a file (read & write data)


# Types of files ----->   1. Text Files(.txt .docx .log etc)    2. Binary Files(.mp4 .mov .png .jpeg etc)


#OPENING & CLOSING A FILE
f = open("Lecture 6/demo.txt", "r")                           # [ open (“file_name”, “mode”) ]

data = f.read()                                               # Here 'data' is variable that stores entire data stored in 'demo.txt'
print(data)                             
print(type(f))                                                # <class 'str'>

f.close()                                                     # Closes the file



# Character    -----    Meaning
#   'r'        -----    open for reading (default)
#   'w'        -----    open for writing, truncating the file first 
#   'a'        -----    open for writing, appending to the end of the file if it exists 
#   'x'        -----    create a new file and open it for writing

#   't'        -----    text mode (default)
#   'b'        -----    binary mode 

#   'r+'       -----    Open for reading and writing. The stream is positioned at the beginning of the file
#   'w+'       -----    Open for reading and writing. The file is created if it does not exist, otherwise it is truncated
#   'a+'       -----    Open for reading and writing. The file is created if it does not exist. The stream is positioned at the end of the file.



#READING A FILE
f = open("Lecture 6/demo.txt","r")      
print (f.read())                                              # Reads entire file
f.close()

f = open("Lecture 6/demo.txt","r")      
print (f.read(25))                                            # Reads first 25 character
f.close()

f = open("Lecture 6/demo.txt","r")      
print ("Line1-", f.readline())                                # Reads one line at a time
print ("Line2-", f.readline())                     
f.close()

f = open("Lecture 6/demo.txt","r")                            # Reads all lines into a list
print(f.readlines())
f.close()

'''
Welcome back Captain. All systems are ready.
This is a demo text.
'''

#WRITING TO A FILE
f = open("Lecture 6/demo.txt","w")      
f.write ("This is a demo line\nThis is demo text_v2")         # Truncates the entire file
f.close()

f = open("Lecture 6/demo.txt","a")      
f.write( "\nThis is a new line with a demo text_v3" )         # Adds to the file
f.close()



f = open("Lecture 6/hello_samplefile.txt","w")                # Can be used to create new files
f.write("This is a sample text")
f.close()

f = open("Lecture 6/hello_samplefile.txt","w+")               # Truncates the entire file and put cursor at beginning where we can write
f.write ("This is a new line\nThis is sample text_v2")
f.close()

f = open("Lecture 6/hello_samplefile.txt","r+")               # Cursor starts at the beginning; writing overwrites existing characters.
f.write("OverRULE")
print(f.read())
f.close()

f = open("Lecture 6/hello_samplefile.txt","a+")               
f.write( "\nThis is a new line with a sample text_v3" )       # Put cursor at the end and adds the text to the file

print("BLANKLINE",f.read())                                   # Prints blank as the cursor is at the end and no text is there

f.seek(0)                                                     # Moves the cursor to the beginning of the file
print(f.read())
f.close()



# OPENING USING 'with' SYNTAX
with open ("Lecture 6/i_am_GONE.txt","w") as f:               # as = alias
    f.write("This is creating using 'with' syntax. \nI will be GONE")

with open ("Lecture 6/i_am_GONE.txt","r") as f:               # It also closes the file automatically
    data = f.read()
    print(data)


# MODULES ---> A module is a file containing code written by somebody else (usually) which can be imported and used in our programs

# PIP   ---> Pip is the package manager for python. You can use pip to install a module on your system ---> 'pip3 install pyjokes'


# DELETING A FILE USING 'os module'
import os 
os.remove("Lecture 6/i_am_GONE.txt")



#Practise Question 1
#1
with open ("Lecture 6/practice1.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n") 
    f.write("using Java. \nI like programming in Java.") 

#2
with open ("Lecture 6/practice1.txt","r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")

with open ("Lecture 6/practice1.txt", "w") as f:
    f.write(new_data)

#3
def check_for_word():
    word = "learning"

    with open("Lecture 6/practice1.txt", "r") as f:
        data = f.read ()

    if(word in data):
        print ("Word Found" )
    else:
        print ("Word not Found")
check_for_word()

#4
def check_for_line():
    word = "Python"
    line_no = 1
    l=[]

    with open ("Lecture 6/practice1.txt", "r") as f:
        for line in f:
            if(word in line):
                l.append(line_no)
            line_no += 1
    
    if len(l) == 0:
        return "Word is not found, -1"
    return f"Word found at these lines: {l}"
print(check_for_line())



#Practise Question 2
with open ("Lecture 6/practice2.txt","w") as f:
    f.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15")

with open ("Lecture 6/practice2.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    print(nums)

    count = 0
    for n in nums:
        if int(n) % 2 == 0:
            count += 1
print("Count of even numbers:", count)



#Practise Question 3
with open ("Lecture 6/practice3.txt","w+") as f:
    f.write ("This is a very secret information\nKeep it confidential")
    f.seek(0)
    data = f.read()

with open ("Lecture 6/practice3copy.txt","w+") as f:
        f.write (data)







