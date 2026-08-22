list_2d=[[1,3,5],[7,11,13]]
print(list_2d[1][2])
list_2d.append([17,23,29])
print(list_2d)
list_2d[1].append(9)
print(list_2d)
list_2d[1].remove(9)
print(list_2d)
list_2d.remove([1,3,5])
print(list_2d)
for i in list_2d:
    for j in i:
        print(j)
for i in range(2):
    for j in range(3):
        print(list_2d[i][j])