def sum(*n):
    print(type(n))
    sum=0
    for i in n:
        sum+=i
    return sum

print(sum(1,2,3,4,5,6,7,8,9,10))

def name(*n):
    for i in n:
        print(i,end=" ",)
name("Mr","Vipin","raj","v")


