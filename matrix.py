import numpy as np
import copy

matA = np.array([1,2,3],
								[4,5,6],
								[7,8,9])
								
matB = copy(matA)			

print('Matrix A is:')
print matA

print('Matrix B is:')
print matB

prodA_Binv = np.dot(matA, np.linalg.inv(matB))

print 'product of A and inverse of B is:'
print prodA_Binv
