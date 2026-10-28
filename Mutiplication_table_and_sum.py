n=int(input("Enter a number "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
s=0
f=1
while f<=n:
    s+=f
    f=f+1
print(s)
# sum=n*(n+1)/2
# print(sum)