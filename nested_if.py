h=int(input("enter hight "))
if h>160:
    print("you can ride ")
    a=int(input("Enter your age "))
    if a>=18:
        print("pay Rs 500")
    else:
        print("pay Rs 250")
else:
    print("You can't take this Ride")