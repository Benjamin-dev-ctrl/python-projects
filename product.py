products={'milk':2.50,'eggs':3.50,'bread':3.99,'water':0.99}
cart={}
for i in products:
    print(i,products[i])
while True:
 product=input('what product do you want?')
 if product == 'stop':
    break
 quantity=int(input('how many products do you want?'))
 cart[product]=quantity
total=0
for i in cart:
   amount= products[i]*cart[i]
   total=total+amount
   print(i, cart[i], products[i], amount)
print('the total price is:', total)