def funtion_1():
    x=1                # x is a local variable of funtion_1()
    def funtion_2():
        #x=2           # here x becomes a local variable so this x will be given  preference 
        print(x)       # here x is an enclosed variable of funtion_1() i.e. funtion_2() enclosed in funtion_1()
    funtion_2()
funtion_1()