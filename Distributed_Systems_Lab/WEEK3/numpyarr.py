import numpy as np

# 1. Array creation
A = np.array ([2,5,10])
print(A.dtype)
B=np.array ([2.4,10.6,5.2])
print(B.dtype)

# Creating sequence of sequence will create 2-dimensional array.
A=np.array([(3,4,5),(12,6,1)])
Z=np.zeros((2,4)) # will create zero matrix of dimension 2x4
print(A,'\n',B)
print(np.ones((3,3))) # will create one’s matrix of dimension 3x3

# To create a sequence of data,
S=np.arange(10,30,5)
print(S) 
print(np.arange( 0, 2, 0.3 )) # it accepts float arguments

#lnstead of step-size, we can specify total number of elements in the array using
S1=np.linspace(0,2,9) # produce 9 numbers starting 0 & ends with 2
print(S1)