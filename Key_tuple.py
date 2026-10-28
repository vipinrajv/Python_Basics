def address(*n,**keyword):
    for i,j in keyword.items():
        print(i,j)
     
    sum=0
    for i in n:
        sum+=i
    print(sum)
    
    
address(1,2,3,4,5,6,7,name="vipin",dep="maths",collage="KU")