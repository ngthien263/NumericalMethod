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
for i in range(n*(n+1)):
    mat[i] = lines[i+1]
mat = np.reshape(mat, (n,n+1))
b = np.zeros((n,1), dtype=float)
for i in range(n):
        b[i] = mat[i][n]
for k in range(n-1):
    for i in range(k+1,n):
        if abs(mat[i][i])<abs(mat[i][k]):
            mat[[k,i]] = mat[[i,k]]
            b[[k,i]] = b[[i,k]]
            break;
for i in range(n):
    for j in range((i+1),n):
        if mat[j][i] == 0: continue
        em = float(mat[j][i]/mat[i][i])
        for k in range(n+1):
            mat[j][k] = mat[j][k] - em*mat[i][k]


x = np.zeros((n,1), dtype=float)
print("\nMatrix after Gassian elimination: \n", mat)
for i in range(n):
        b[i] = mat[i][n]
x[n-1][0]=b[n-1]/(mat[n-1][n-1])
print(x[n-1][0])
for i in range(n-2,-1,-1):
    x_sum = 0;
    for j in range((i+1),n):
        x_sum += mat[i][j]*x[j]
    x[i] = (b[i] - x_sum)/mat[i][i]
print("\nx=\n", x)