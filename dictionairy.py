sports={'basketball':5,'f1 racing':2, 'soccer':11, 'baseball':7}
print(sports['basketball'])
sports['tennis']=2
print(sports)
sports['f1 racing']=5
print(sports)
del sports['soccer']
print(sports)
for i in sports:
    print(i,sports[i])