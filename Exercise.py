import os

f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\data.txt","w")
f1.write("Python\nJava\nC++")
f1.close()
f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\data.txt","r")
print(f1.read())
f1.close()
f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\data.txt","a")
f1.write("\nJavaScript")
f1.close()
f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\data.txt","r+")
print(f1.read(6))
f1.seek(0)
f1.write("HELLO!")
f1.seek(0)
print(f1.read())
f1.close()


f2=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\temp.txt","w+")
f2.write("1\n2\n3")
f2.seek(0)
print(f2.read())
f2.close()


f3=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\log.txt","a+")
f3.write("Program started")
f3.seek(0)
print(f3.read())

os.rename("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\temp.txt","C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\numbers.txt")
print(os.path.exists("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\numbers.txt"))
print(os.remove("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\numbers.txt"))
