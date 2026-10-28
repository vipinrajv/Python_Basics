mark=input("Enter the mark ")
mark=int(mark)
if mark>=90 and mark<=100:
    print("A GRADE ")
elif mark>=75 and mark<=89 :
    print("B GRADE ")
elif mark>=50 and mark<=74:
    print("C GRADE ")
elif mark<50 and mark>=0:
    print("Failed ")    
else:
    print("INVALID")