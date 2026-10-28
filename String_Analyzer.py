strng=input(" Enter a sentence ")
print(strng.upper())
print(strng.lower())
l=1
for i in strng:
    if i==" ":
        l+=1
print(f"{l} words ")
print(strng[::-1])
print(strng.replace(" ","-"))



