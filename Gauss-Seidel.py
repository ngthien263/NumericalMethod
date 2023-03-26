import sys,string,os
import numpy as np
##input matrix
input_folder =  'F:\\ppt'
input_exec =  '"F:\\ppt\\input.exe"'
os.chdir( input_folder)
os.system(input_exec)
input_file = 'F:\\ppt\\input.txt'
file = open(input_file, 'r')
lines = file.readlines()
file.close()
n = int(lines[0])
mat = np.zeros((n*(n+1)), dtype=float)
b = np.zeros((n,1), dtype=float)
for i in range(n*(n+1)):
    mat[i] = lines[i+1]
mat = np.reshape(mat, (n,n+1))

#pivot
for k in range(n-1):
    for i in range(k+1,n):
        if abs(mat[i][i])<abs(mat[i][k]):
            mat[[k,i]] = mat[[i,k]]
            b[[k,i]] = b[[i,k]]
            break

xk = np.zeros((n,1), dtype = float)
xk_1 = xk.copy()
b = np.zeros((n,1), dtype=float)
R = np.zeros((n,1), dtype=float)
for i in range(n):
        b[i] = mat[i][n]
###Gauss-Seidel method
stop_cond = 1.0e-4
print("\n\nGauss-Seidel: \n")
k = 0
i=0
while k < 20:
    for i in range(n):
        Rsum = 0
        for j in range(n):
            if j != i:
                Rsum += mat[i][j] * xk_1[j]
        xk_1[i] = (b[i] - Rsum)/mat[i][i]
    k = k+1
    print(k,"th iteration: \nx =\n", xk_1)
    # if xk_1[i] - xk[i] < stop_cond:
    #     break
    xk = xk_1.copy()

