def loop():
    for i in range(1,11):
        print(i)
loop()

def sum(n1,n2):
    print(n1+n2)

sum(10,11)

def bill(name,amount,date):
    print(f"Name: {name}")
    print(f"Bill amount: {amount}")
    print(f"Date: {date}")

name=input("Enter your name ")
amount=int(input("Enter amount "))
date=input("Enter due date ")
bill(name,amount,date)


def sum(a,b):
    c=a+b
    return c
print(sum(10,20))
print(sum(20,30))
print(sum(30,40))


a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))

def sum(x,y):
    z=x+y
    return z

print(sum(a,b))

def fullname(firstn,lastn):
    fulln= firstn.capitalize() +" "+ lastn.capitalize()
    return fulln

fn=input("Enter first name ")
ln=input("Enter last name ")
print(fullname(fn,ln))