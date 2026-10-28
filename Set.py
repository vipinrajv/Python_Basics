fruits={"apple","banana","mango","coconut","blue berry","black berry"}
print(fruits)
#print(dir(fruits))
fruits.remove("apple")
print(fruits)
fruits.add("grape")
print(fruits)
fruits.pop()
print(fruits)
fruits_2={"mango","coconut","blue berry","grape","pineapple"}
union=fruits.union(fruits_2)
print(union)
intersection=fruits.intersection(fruits_2)
print(intersection)

A={1,2,3,4,5,6,7,8,9}
B={6,7,8,9,10,11,12,13}
diff=A.difference(B)
print(diff)
print(1 in A)