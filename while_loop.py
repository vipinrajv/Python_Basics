n=input("Enter your Name ")
while n=="":
    print("you have not entered your name")
    n=input("Enter your Name ")
print(f"Hello {n}")


a=int(input("Enter age "))
while a<18:
    print("NOT VALID ")
    a=int(input("Enter age "))
print("VALID")

f=input("Enter your favorate food(enter Q to Quit) ")
while f!="Q":
    f=input(f"your favorate food is {f} Enter another food ")
print("see you soon")

n=int(input("Enter a number between 1 and 10 "))
while n<1 or n>10:
    n=int(input("INVALID NUMBER enter again  "))
print(f"Entered number is {n}")