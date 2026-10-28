capitals={"USA":"Washington DC","India":"New Delhi","Japan":"tokiyo","Russia":"moscow"}
print(capitals)
print(capitals)
print(capitals.get("India"))
if capitals.get("Chaina"):
    print("capital exist")
else:
    print("Capital doesnot exist")
if capitals.get("USA"):
    print("capital exist")
else:
    print("Capital doesnot exist")
print("------------------------------------------------------------------------------------------------------------------------------------")
capitals.update({"Germany":"Berlin"})
print(capitals)
capitals.update({"USA":"Detroit"})
print(capitals)
capitals.update({"Usa":"Detroit"})
print(capitals)
capitals.pop("Usa")
print(capitals)
capitals.popitem()
print(capitals)
print("---------------------------------------------------------------------------------------------------------------")
keys=capitals.keys()
print(keys)
for i in keys:
    print(i)
values=capitals.values()
print(values)
for i in values:
    print(i)
items=capitals.items()
print(items)
for i in items:
    print(i)
for i,j in items:
    print(i,j)
print(capitals.get("USA"))
print(capitals.clear())