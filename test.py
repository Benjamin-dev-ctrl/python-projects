countries_and_capitals={'Spain':'Barcelona','France':'Paris','Italy':'Rome'}
print(countries_and_capitals['Italy'])
countries_and_capitals['Brittain']='London'
print(countries_and_capitals)
del countries_and_capitals['France']
print(countries_and_capitals)
countries_and_capitals['Spain']='moscow'
print(countries_and_capitals)
for keys in countries_and_capitals:
    print(keys,countries_and_capitals[keys])
for keys,value in countries_and_capitals.items():
    print(keys,value)