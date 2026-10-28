f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\file_1.txt","w")
f1.write("Hi I am Vipin")
f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\file_1.txt","r")
print(f1.read())
print("-----------------------------------------------------------------------------------------------------------------------------")
f1=open("C:\\Users\\91996\\Desktop\\python basics\\File_Handling\\file_1.txt","r+") # First read then write
print(f1.read())
f1.seek(0)
f1.write("  hello")
