even=[]
for i in range(1,11):
    even.append(i*2)
print(even)
print("-------------------------------------------\n")

e=[i*2 for i in range(1,11)]           #[expression for value in iterable if condition]
print(e)
print("-------------------------------------------\n")

print([i*i for i in range(1,11) ])
print("-------------------------------------------\n")

fruits=["apple","banana","banana","mango","coconut","blue berry","black berry"]
print(fruits)
print([f.upper() for f in fruits])
print(f"First characters in Fruits are {[i[0] for i in fruits]}\n")

print("-----------------WITH CONDITION--------------------------\n")
n=[1,4,-7,4,-8,-4,5,-8,-6,-4,1]
print(f"Positive numbers are { [p for p in n if p>=0]}")
print(f"Negative numbers are {[i for i in n if i<=0]}")
print(f"Even numbers are {[e for e in n if e%2==0]}")
print(f"Odd numbers are {[o for o in n if o%2!=0]}\n")

print("-------------------------------------------\n")
m=[39,15,85,34,7,89,75,45,23,76,12,100]
print(f"Pass= {[p for p in m if p>=30]}")
print(f"Fail= {[f for f in m if f<30]}")