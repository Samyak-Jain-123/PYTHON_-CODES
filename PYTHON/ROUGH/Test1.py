import numpy as np

str_arr = np.array([1, 2, 3], dtype="U")
print(str_arr, str_arr.dtype)

float_arr = np.array([1, 2, 3], dtype="i")
print(float_arr, float_arr.dtype)


# try:
#     x=10
#     a = x/0
#     print(a)

# except :
#     print("ERROR")
# print("Hello")

# a =10
# b =a
# b=b+10
# print(a,b)



# try:
#   print(x)
# except ZeroDivisionError as s:
#   print(s)
#   print("Variable x is not defined")
# except Exception as e:
#   print(e)
#   print("Something else went wrong")
