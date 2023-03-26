import numpy as np
import os
##input matrix
input_folder =  'F:\\ppt\\chapter3'
input_exec =  '"F:\\ppt\\chapter3\\input.exe"'
os.chdir( input_folder)
os.system(input_exec)
input_file = 'F:\\ppt\\chapter3\\input.txt'
file = open(input_file, 'r')
lines = file.readlines()
file.close()
n = int(lines[0])
mat = np.zeros((n*n), dtype=float)
for i in range(n*n):
    mat[i] = lines[i+1]
mat = np.reshape(mat, (n,n))
x=np.ones((n,1), dtype = float)
l = 0
while l < 30:
    x = mat @ x
    lmbda = max(abs(x))
    for i in range(n):
        x[i] = x[i]/ lmbda
    l += 1
    print("λ = ", lmbda,"v = ", np.reshape(x,(1,n)))

