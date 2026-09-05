numb=(1,2,3,4,5,6,7,8,9,10)
#numb[3]=2

print(numb[6])

set1={1,2,3,3,4,4,5,6,7,7,8}
print(set1)
set1.add(11)
print(set1)
set1.remove(7)
print(set1)
set2={8,9,10,11,12,13}
print(set1.intersection(set2))
print(set1.union(set2))
print(set2.difference(set1))
print(set1.difference(set2))
