def address(**keyword):
    for i in keyword.keys():
        print(i)
    print("--------------------")
    for j in keyword.values():
        print(j)
    print("--------------------")
    for i,j in keyword.items():
        print(i,j)

address(name="vipin",dep="maths",collage="KU")
