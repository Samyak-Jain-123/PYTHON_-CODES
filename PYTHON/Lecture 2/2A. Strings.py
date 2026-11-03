#STRINGS
print("""This is a multi line string
with triple quotes.""")
print("This is a multi line string\nwith slash n.")     # \n = new line
print("This is a multi line string\twith slash t.")     # \t = tab space



#Concatenation And LENGTH Function
str1 = "Samyak"
print(str1)
print (len(str1))

str2 = "Jain"
print(str2)
print (len(str2))

str3 = str1 + " " + str2
print (str3)
print (len(str3))



#Indexing
str1 = "Samyak Jain"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
print(str1[7])
print(str1[8])
print(str1[9])
print(str1[10])



#Slicing
str1 = "Samyak Jain"
print(str1[0:5])            # ending idx is not included
print(str1[0:6])
print(str1[:6])             # [0:6]
print(str1[7:])             # [7:11] OR [7:len(str1)]



#String Function
str1 = "samyak Jain"
print(str1)

print(str1.endswith("ain"))         # returns true if string ends with substring
print(str1.endswith("yak"))

print(str1.capitalize())            # capitalizes 1st char (creates a new string)
print(str1)                         

print(str1.replace("a","o"))        # replaces all occurrences of old with new (creates a new string) 
print(str1.replace("Jain","Sam"))

print(str1.find("a"))               # returns 1st index of 1st occurrence
print(str1.find("yak"))
print(str1.find("q"))               # returns -1 if substring is not found

print(str1.count("a"))              # counts the occurrence of substr in string
print(str1.count("o"))


