matrix_a=[[1,2,3],[4,5,6],[7,8,9]]
matrix_b=[[10,11,12],[13,14,15],[16,17,18]]
for i in range(0,3):
    for j in range(0,3):
     print(matrix_a[i][j]+matrix_b[i][j],end=' ')
    print()

matrix_a=[[1,2,3],[4,5,6],[7,8,9]]
matrix_b=[[10,11,12],[13,14,15],[16,17,18]]
matrix_c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
     matrix_c[i][j]=matrix_a[i][j]-matrix_b[i][j]
print(matrix_c)
    
