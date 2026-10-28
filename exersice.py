menu={"normal mandhi":200,"alfam":220,"peri peri":240,"Honey chilly":250}
cart=[]

print("--------------MENU---------------------")
for i,j in menu.items():
    print(f"{i:20}:{j:.2f}")
print("---------------------------------------")

while True:
    food=input("Enter the food you want to buy(Q to Quit):\n")
    if food.upper()=="Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

total=0
print("-------------Your Order----------------")
for food in cart:
    total+=menu.get(food)
    print(f"{food:20}:{menu.get(food):.2f}")
print("--------------------------------------")
print(f"total{total:20}")
