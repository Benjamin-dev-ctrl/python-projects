list2d=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    for j in range(0,3):
        print(list2d[i][j],end=' ')
    print()
for i in range(3):
    print(list2d[0][i],end=' ')
print()
for i in range(3):
    print(list2d[i][1],end=' ')
print()
for i in range(2,-1,-1):
    print(list2d[2][i],end=' ')
print()
for i in range(2):
    for j in range(3):
        print(list2d[i][j],end=' ')
    print()
print()
for i in range(2):
    for j in range(3):
        print(list2d[i+1][j])