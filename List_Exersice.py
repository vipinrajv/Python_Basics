#   SHOPPING CART
food=[]
price=[]
while True:
    f=input("Enter the food you want to buy (Q to Quit): ")
    if f.upper()=="Q":
        break
    else:
        food.append(f)
        p=int(input("Enter the price of the food: "))
        price.append(p)
for i in food:
    print(i)
total=0
for i in price:
    total+=i
print(f"Total cost= {total}")