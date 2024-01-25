# 2. Find the sum of columns and rows using axis.
# 4. Write a program to transpose a given matrix.
# 5. Write a program to add two matrices.
# 6. Write a program to find element wise product Between two matrices.

import numpy as np
A = np.array( [[1,1],[0,1]] )
B = np.arange(12,20,2).reshape(2,2)
print("Matrix A:", A, "\nMatrix B:", B, sep='\n')

# q2
print("\nEach column sum of B:")
print(B.sum(axis=0)) # sum of each column
print("\nEach row sum of B:")
print(B.sum(axis=1)) # sum of each row

# q4
print("\nTranspose of B is\n",B.T)

# q5
print("\nSum of A and B is\n",A+B)

# q6
print("\nElementWise product of A and B is\n",A*B) # elementwise product

