#NumPy (Numerical Python) 
# NumPy is an open-source Python library, which was created in 2005 by Travis Oliphant and is used for numerical computing. 
# It is widely used in fields that involve heavy-data processing, such as data science, engineering, AI & ML. 
# It provides tools for working efficiently with arrays, matrices, and mathematical functions.

# NumPy introduces a new data structure called the ndarray (n-dimensional array),
# which is much faster and more memory-efficient than Python’s built-in lists for numerical operations.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

import numpy as np
print(np.__version__)                                       # 2.4.6


my_list = [1, 2, 3, 4, 5] 
print(my_list)                                              # [1, 2, 3, 4, 5]
print(type(my_list))                                        # <class 'list'>
my_list = my_list * 2
print(my_list)                                              # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


my_arr = np.array([1, 2, 3, 4, 5])
print(my_arr)                                               # [1 2 3 4 5]
print(*my_arr)                                              # 1 2 3 4 5
print(type(my_arr))                                         # <class 'numpy.ndarray'>
my_arr = my_arr * 2
print(my_arr)                                               # [ 2  4  6  8 10]
print(*my_arr)                                              # 2 4 6 8 10





# Performance Comparison
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object (ndarray) that is up to 50x faster than traditional Python lists.

import time
size = 10_000_000 # large data set of 10 million numbers


# Python Lists
python_list = list(range(size))
start = time.time()
list_squared = [x**2 for x in python_list]                  # Square of all nums
end = time.time()
print("Python list time:", end - start, "seconds")


# NumPy Arrays
np_array = np.array(python_list)
start = time.time()
array_squared = np_array ** 2                               # Vectorized operation
end = time.time()
print("NumPy array time:", end - start, "seconds")



# 1.Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# This behavior is called locality of reference in computer science.

# 2.Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.





# Memory Usage comparison
# NumPy store elements in contiguous memory (better cache performance).

import sys
print("Python list size:", sys.getsizeof(python_list) * len(python_list))
print("NumPy array size:", np_array.nbytes)





# Multi-dimensional Arrays
# 0D Arrays
arr1 = np.array( 'A' )
print(arr1) 
print(arr1.ndim, arr1.shape)

# 1D Arrays
arr2 = np.array( [1, 2, 3] )
print(arr2) 
print(arr2.ndim, arr2.shape)

# 2D Arrays 
arr3 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
print(arr3) 
print(arr3.ndim, arr3.shape)

# 3D Arrays
arr4 = np.array([ [['A','B','C'], ['D','E','F'], ['G','H','I']],
                  [['J','K','L'], ['M','N','O'], ['P','Q','R']],
                  [['S','T','U'], ['V','W','X'], ['Y','Z','&']]  ])
print(arr4) 
print(arr4.ndim,arr4.shape)





# Chain Indexing
print(arr4[2][0][0])
print(arr4[0][0][0])
print(arr4[1][1][0])
print(arr4[2][0][0] + arr4[0][0][0] + arr4[1][1][0])


# Multidimensional Indexing
print(arr4[2,0,0])
print(arr4[0,0,0])
print(arr4[1,1,0])
print(arr4[2,0,0] + arr4[0,0,0] + arr4[1,1,0])


arr = np.array([1, 2, 3, 4, 5])

# Fancy Indexing
idx = [0, 1, 4]
print(arr[idx])                                             # print nums at given indices


# Boolean Indexing
print(arr[arr > 2])                                         # print nums greater than 2
print(arr[arr % 2 ==0])                                     # print even num



# Slicing
arr = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12], 
                [13, 14, 15, 16]])

print(arr[1])
print(arr[-1])

print(arr[::2])
print(arr[::-1])
print(arr[::-2])


print(arr[:,1])
print(arr[:,-1])

print(arr[:, ::2])
print(arr[:, ::-1])
print(arr[:, ::-2])


print(arr[0:2, 0:2])
print(arr[0:2, 2:])
print(arr[2:, 0:2])
print(arr[2:, 2:])
print(arr[1:3, 1:3])

print(arr[::2, ::2])
print(arr[::-1, ::-1])
print(arr[::-2, ::-2])



# Creating NumPy Arrays - from scratch
arr1 = np.zeros((3, 4))                                     # 3x4 array of 0s
print(arr1, arr1.shape)

arr2 = np.ones((3, 3))                                      # 3x3 array of 1s
print(arr2, arr2.shape)

arr3 = np.full((2, 3), 5)                                   # 2x3 array of 5s
print(arr3, arr3.shape)

arr4 = np.eye(3)                                            # Identity matrix of 3x3
print(arr4, arr4.shape)

arr5 = np.arange(1, 20, 2)                                  # Elements in range (1, 20)
print(arr5, arr5.shape)

arr6 = np.linspace(0, 10, 5)                                # Evenly spaced array
print(arr6, arr6.shape)



# Data Types in NumPy
# #i - integer
# #b - boolean
# #u - unsigned integer
# #f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# #S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
    


# Useful Attributes
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(arr.shape)                                            # Dimensions - (4 x 3)
print(arr.size)                                             # Total elements - (12)
print(arr.ndim)                                             # Number of dimensions - 2
print(arr.dtype)                                            # Data type object - int64
print(arr.itemsize)                                         # Size of each element in bytes - 8 for int64



# dtype & astype
arr1 = np.array([1.3, 2.87, 3.13], dtype="f")
print(arr1, arr1.dtype)                                     # [1.3  2.87 3.13] float32

arr2 = np.array([1.3, 2.87, 3.13], dtype="U")
print(arr2, arr2.dtype)                                     # ['1.3' '2.87' '3.13'] <U4

arr3 = arr1.astype('int64')
print(arr3, arr3.dtype)                                     # [1 2 3] int64



# Reshaping
arr1 = np.array([1, 2, 3, 4, 5, 6])
print(arr1, arr1.shape)

arr2 = arr1.reshape((2, 3))                                 # converts (1x6) => (2x3)
print(arr2, arr2.shape)

arr3 = arr2.flatten()                                       # converts 2D => 1D
print(arr3, arr3.shape)


# COPY vs VIEW
# Copy is a new array, and the view is just a view of the original array.
# The copy owns the data and any changes made to the copy will not affect original array, and vice-versa.
# The view does not own the data and any changes made to the view will affect the original array, and vice-versa.
# Views are fast and memory-efficient (no data duplication) whereas Copies are safe but slower and use more memory.


arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.copy() 
arr1[0] = 42
print(arr1)                                                 # [42  2  3  4  5]
print(x)                                                    # [1 2 3 4 5]


arr2 = np.array([1, 2, 3, 4, 5])
x = arr2.view()
arr2[0] = 42
print(arr2)                                                 # [42  2  3  4  5]
print(x)                                                    # [42  2  3  4  5]


# Slicing a list returns a copy but slicing a NumPy array returns a view - for efficiency.


# Sliced List is a COPY
my_list = [1, 2, 3, 4, 5]
copy_list = my_list[1:4]                                    # [2, 3, 4]
copy_list[1] = 33
print(copy_list)                                            # [2, 33, 4]
print(my_list)                                              # [1, 2, 3, 4, 5] - remains same

# Sliced Array is a VIEW
np_arr = np.array([1, 2, 3, 4, 5])
view_arr = np_arr[1:4]                                      # [2 3 4]
view_arr[1] = 33
print(view_arr)                                             # [ 2 33  4]
print(np_arr)                                               # [ 1  2 33  4  5] - changes

# Creating a COPY for Array
np_arr = np.array([1, 2, 3, 4, 5])
copy_arr = np_arr[1:4].copy()                               # [2 3 4]
copy_arr[2] = 44
print(copy_arr)                                             # [ 2  3 44]
print(np_arr)                                               # [1 2 3 4 5] - remains same

