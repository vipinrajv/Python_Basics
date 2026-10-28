user_name=input("Enter user name ")
if len(user_name)>12:
    print("Name must not contain 12 character")
elif user_name.isalpha()==False:
    print("You cannot enter number or space")
else:
    print("Valid user name")
