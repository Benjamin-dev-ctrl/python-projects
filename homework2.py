import random
matrix_3x3=[[0,0,0],[0,0,0],[0,0,0]]
max=0
for i in range(0,3):
    print()
    for j in range(0,3):
        matrix_3x3[i][j]=random.randint(0,9)
        print(matrix_3x3[i][j],end=' ')
        if matrix_3x3[i][j]>max:
            max=matrix_3x3[i][j]
print()
print(max)

    

    

