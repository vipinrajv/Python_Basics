age=int(input("enter your age "))
if age>=18:
    print("Your are now signed up")


name=input("enter your name ")
if name !="":
    print(f"my name is {name}")

ph_no=int(input("Enter Phone Number "))
Ph_no_string=str(ph_no)
if len(Ph_no_string)>10: #len() is string funtion
    print("INVALID")
