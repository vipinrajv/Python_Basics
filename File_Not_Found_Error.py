try:
    f1=open("file2.txt","r")
    print(f1.read())
except FileNotFoundError:
    print("No Such file")