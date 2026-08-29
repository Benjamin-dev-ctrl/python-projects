list2d=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(2,-1,-1):
    print(list2d[i][2])

for i in range(0,3):
    for j in range(2,-1,-1):
        print(list2d[i][j],end=' ')
    print()

for i in range(0,3):
    print(list2d[i][i])

for i in range(2,-1,-1):
    print(list2d[i][i])

for i in range(2,-1,-1):
    print(list2d[1][i])

for i in range(0,3):
    for j in range(2,0,-1):
        print(list2d[i][j],end=' ')
    print()

