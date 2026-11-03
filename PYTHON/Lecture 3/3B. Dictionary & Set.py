# DICTIONARY

d = {                                     # It is used to store data values in 'key : value' pairs
 "key"         : "value",                    
 "name"        : "Sam",                   # Values can be lists, but keys cannot be lists
 9.6           : "cgpa",                  # i.e Keys are immutable, but values can be changed
 ('P','C','M') : "subjects",                              
 "marks"       : [98, 97, 95],            # They are unordered, mutable & don't allow duplicate keys   
 "job"         : None                
}
print(d)
print(type(d))                            # <class 'dict'>


print(d["key"])                           
print(d["name"])
print(d[9.6])
print(d[('P','C','M')])                   # There is no indexing in dict (only keys are used)
print(d["marks"])
print(d["job"])


d["name"] = "Samyak Jain"                 # Change value
d["college"] = "XYZ"                      # Adds a new key and value
print(d)



#Nested dictionary
score = {
    "key"      : "value",
    "name"     : "Samyak",
    "subjects" : { 
        "phy"  : 97,
        "chem" : 98,
        "math" : 95}
}
print (score)
print (score["subjects"])
print (score["subjects"]["chem"])



# Specific function for dict                             
print(score.keys())                       # Returns all keys
print(type(score.keys()))                 # <class 'dict_keys'>

print(score.values())                     # Returns all values
print(type(score.values()))               # <class 'dict_values'>

print(score.items())                      # Returns all (key, value) pairs as tuples
print(type(score.items()))                # <class 'dict_items'>


print(score.get("name"))                  # Returns None if key is not found
print(type(score.get("name")))            # <class 'str'>
'OR'
print(score["name"])                      # Raises KeyError if key is not found
print(type(score["name"]))                # <class 'str'>


score.update({ "job" : None })            # Adds a new key and value
score.update({ "name" : "SAM" })          # Change value
'OR'
score["job"] =  None                      # Adds a new key and value
score["name"] = "SAM"                     # Change value                     
print(score)

score.pop("name")                            
'OR'                                      # removes the specified key
del score["key"]
print(score)

score.popitem()                           # removes the last item                   
print(score)



#SETS
s = {1, 2, 2, 2, "ha", "sam", "sam"}      # Each element in the set must be unique & immutable
                                                 
print (s)                                 # repeated elements stored only once
print (type (s))                          # <class 'set'>
print (len(s))


#Specific function for sets  
s.add (3)                                 # adds an element
print(s)

s.remove(2)                               # removes the element
print(s)

s.pop()                                   # removes any one value from the set
print(s)
 
s.clear()                                 # empties the set
print(s)


s1={1,2,3}
s2={2,3,4}

print(s1.union(s2))                       # combines both set values & returns new

print(s1.intersection(s2))                # returns common values from both sets   



