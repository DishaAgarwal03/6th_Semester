import numpy as np

# Stacking together different arrays
A1=np.array([(3,4,5),(12,6,1)])
A2=np.array([(1,2,6),(-4,3,8)])
D1=np.vstack((A1,A2))
print(D1)
D2=np.hstack((A1,A2))
print(D2)

# Stacking 1-D array into 2-D array (column wise)
a = np.array([4.,2.])
b = np.array([3.,8.])
print(np.column_stack((a,b))) # returns a 2D array
print(np.hstack((a,b)))
# print(np.hstack((a[:,newaxis],b[:,newaxis]))) # the result is the same
