# Array ---> It is a data structure which is used to store the same type of values (Homogeneous data types)

import array as a

arr1 = a.array("i",[0,1,2,3,4,5,6,7])   
print(arr1)                                                 # array('i', [0, 1, 2, 3, 4, 5, 6, 7])
print(*arr1)                                                # 0 1 2 3 4 5 6 7
print(type(arr1))                                           # <class 'array.array'>


# TypeCode  ---  C Type  ---  Python Type ---  Minimum Size 

#   'b'        signed char       int               1 Byte
#   'i'        signed int        int               4 Byte
#   'f'         float           float              4 Byte
#   'd'        double           float              8 Byte


#1
for i in arr1:
    print(i,end=" ")

#2
print(f"Length = {len(arr1)}")

#3
print(f"SUM = {sum(arr1)}")
"OR"
total=0
for i in arr1:
    total+=i
print("SUM =",total)

#4
print("MAX =",max(arr1))
print("MIN =",min(arr1))

#5
print("AVERAGE =", total/len(arr1))

#6
print("FIRST =",arr1[0])
print("LAST =",arr1[len(arr1)-1])






