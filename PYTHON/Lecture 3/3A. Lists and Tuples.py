#LISTS
l = [94, 87, 95, 66.5, 45]

print (l)
print (type (l))                 # <class 'list'>

print(len(l))                    # Length function

print(l[0])                      # Indexing
print(l[1])
print(l[2])
print(l[3])
print(l[4])

print(l [1:4])                   # Slicing
print(l [:4])
print(l [1:])



#Specific function for lists
l = [1,2,4,3]
print(l)


l.append(2)                      # adds one element at the end
print(l)

l.sort( )                        # sorts in ascending order
print(l)

l.sort( reverse = True )         # sorts in descending order
print(l) 

l.reverse()                      # reverses list
print(l) 

l.insert(2,3)                    # insert element at index (idx,value)
print(l) 

l.remove(3)                      # removes first occurrence of element
print(l) 

l.pop(4)                         # removes element at idx
print(l) 


l1=[1,2,3,4]
l2=[5,6,7,8]
print(l1 + l2)                
'OR'                             #[1, 2, 3, 4, 5, 6, 7, 8]
l1.extend(l2)
print(l1)


l1=[1,2,3,4]
l2=[5,6,7,8]
l1.append(l2)                    #[1, 2, 3, 4, [5,6,7,8]]
print(l1)


l = [1, 2, 1]
cl = l.copy()                    #creates a shallow copy of list
cl.reverse()

if (l == cl): 
    print ("palindrome")
else:
    print ("NOT palindrome")



#TUPLES
tup=(94, 87, 95, 66.5, 45)

print (tup)
print (type (tup))               # <class 'tuple'>

print(len(tup))                  # Length function

print(tup[0])                    # Indexing
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

print(tup [1:4])                 # Slicing
print(tup [:4])
print(tup [1:])


# Tuples are immutable, unlike Lists that are mutable

#Specific function for tuples
tup = (1, 2, 3, 2)
print(tup)


print (tup.index(2))             # returns index of first occurrence

print (tup.count(2))             # counts total occurrences








