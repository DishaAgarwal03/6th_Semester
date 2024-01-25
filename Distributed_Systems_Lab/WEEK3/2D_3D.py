import numpy as np

# 2- Dimensional array (Matrix)
a = np.arange(15).reshape(3, 5)
#to check the dimension
print(a.shape)
print(a.size) # will return total elements in matrix 
# to transpose a matrix
print(a.T)

# 3- Dimensional array
c = np.arange(24).reshape(2,3,4) # 1st value indicates (no of planes) (3,4) is the dimension
print(c)
print(c.shape) 
print(c[1,...]) # equal to c[1,:,:] # will fetch all elements of 2nd plane
print(c[...,2]) # equal to c[:,:,2]