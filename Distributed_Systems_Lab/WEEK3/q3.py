# 3. Operations on Arrays (use numpy wherever required):
# a) Create array from list with type float
# b) Create array from tuple
# c) Creating a 3X4 array with all zeros
# d) Create a sequence of integers from 0 to 20 with steps of 5
# e) Reshape 3X4 array to 2X2X3 array
# f) Find maximum and minimum element of array, Row wise max and min, column wise max
# and min and sum of elements. (Use functions max(), min(), sum())

import numpy as np
# a 
a = np.array( [20.34,30.3,40.22,50.2] )
# b 
b = np.array( (2,0,4,5) )
# c 
c=np.zeros((3,4))
# d 
d = np.arange(0,25,5)
# e 
e = c.reshape(2,2,3)
f = np.arange(9).reshape(3,3)
print("\nA:",a,"\nB:",b,"\nC:",c,"\nD:",d,"\nE:",e, "\nF: ", f, sep='\n')

# f 
print("\nMax and Min of A: ", max(a), min(a))
print("Row wise max of F:", f.max(axis=1))
print("Row wise min of F:", f.min(axis=1))
print("Column wise max of F:", f.max(axis=0))
print("Column wise min of F:", f.min(axis=0))
print("Sum of elements of F:", f.sum())









# import numpy as np

# # Array operations

# b = np.arange( 4 )
# c = a-b
# print(b)
# print(c)
# print(b**2)
# print(10*np.sin(a))
# print(a<35)


# # Matrix operations
# A = np.array( [[1,1],[0,1]] )
# B = np.array( [[2,0],[3,4]] )
# print(A*B) # elementwise product
# print(A.dot(B)) # matrix product
# # (OR)
# print(np.dot(A, B))
# b = np.arange(12).reshape(3,4) # another matrix product
# print(b)
# print(b.sum(axis=0)) # sum of each column
# print(b.sum(axis=1)) # sum of each row


# # Indexing, Slicing & Iterating Array
# a = np.arange(10)**3
# print(a)
# print(a[2:5])
# print(a[0:6:2])
# b=np.arange(20).reshape(5, 4)
# print(b[2,3]) 
# print(b[0:5,1]) # or b[:5,1] or b[:,1] 
# print(b[-1,:]) # will fetch last row
# print(b[:,-1]) # will fetch last col
# for row in b:
#     print (row) # will print every row
# for element in b.flat:
#     print (element) # will show all elements of b in 1-D array
    
    
# # Changing the shape of a matrix
# print(b.ravel()) # returns the array flattened to (1x20)
# # Later, we can convert 5x4 matrix into 4x 5 matrix using
# B1=b.reshape(4,5)
# print(B1)


# # Indexing with array of indices
# a = np.arange(12)**2
# i = np.array( [ 1,1,3,8,5 ] )
# print(a[i]) 
# # the first 12 square numbers
# # an array of indices
# # the elements of a at the positions i
# j = np.array( [ [ 3, 4], [ 9, 7 ] ] ) # a bidimensional array of indices
# print(a[j])
# # the same shape as j
