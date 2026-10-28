strng=input("Enter a word ")
if strng==strng[::-1]:
    print("palindrome")
else:
    print("NOT palindrome")
print(f" first word apperas {strng.count(strng[0])} times ")