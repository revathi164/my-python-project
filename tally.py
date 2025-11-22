from sys import modules

import numpy as np

# print(np.__version__)
#
# my_list = [1,2,3] * 2
#
# print(my_list)

# array = np.array([1,2,3,4,5]) * 2
# print(array)
# print(type(array))

# array = np.array([[["a","b","c"],["d","e","f"],["g","h","i"]],
#                   [["j","k","l"],["m","n","o"],["p","q","r"]],
#                   [["s","t","u"],["v","w","x"],["y","z"," "]]])
# print(array.ndim)
# print(array.shape)
# print(array[0][0][0])
# print(array[1,1,1])
#
# word = array[0,0,0] + array[1,0,2] + array[1,0,2]
# print(word)

# ============ reshape() =======================

# array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# array = array.reshape(-1,2)
#
# print(array.shape)
# print(array)

# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])

# array[start:end:step]

# print(array[::-2])

import numpy as np
from matplotlib.style.core import library

# my_list = np.array([[1,2,3.5],[4,5,6]],int)
#
# print(my_list)
# print(type(my_list))
# print(my_list.shape)
# print(my_list.ndim)
# print(my_list.size)
# print(np.zeros((3,3)).dtype)


# array1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# array2 = np.array([[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
#
# sum_ = array1+array2
# print(sum_)
# sub_ = array1-array2
# print(sub_)
# mul_ = array1*array2
# print(mul_)
# div_ = array1/array2
# print(div_)
# #
#
# print(sum_.size)
# print(sum_.shape)
# print(len(sum_))
# print(sum_.ndim)
#
#
# print(sub_.size)
# print(sub_.shape)
# print(len(sub_))
# print(sub_.ndim)
#
# print(mul_.size)
# print(mul_.shape)
# print(len(mul_))
# print(mul_.ndim)
#
# print(div_.size)
# print(div_.shape)
# print(len(div_))
# print(div_.ndim)


# dim = input("enter your dimension(1dim, 2dim, 3dim) : ")
#
# if dim == "1dim" :
#     array_1 = list(input("Enter the array(enter with out space) : "))
#     array_2 = list(input("Enter the array(enter with out space) : "))
#
#
#     array_list1 = np.array(array_1,dtype = int)
#     array_list2 = np.array(array_2,dtype = int)
#     print(array_list1 + array_list2)
#
# elif dim == "2dim" :
#     rows = int(input("Enter the number of rows : "))
#     for r in range(rows):
#         array = list(input("Enter the array(enter with out space) : "))
#     print(array)
#

# array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# array2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# print(array+array2)

# empty_ = np.empty((3,),int)
# print(empty_)

help()
