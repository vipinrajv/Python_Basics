import equations
import cap
import calculator

print(f"Square of 2 is {equations.square(2)}")
print(f"Cube of 3 is {equations.cube(3)}")
print(f"Area of a circle with radius 3 is {equations.c_area(3)}")

print("---------------------------------------------------------")

print(f"Capital of india is {cap.capitals.get("India")}")

print("---------------------------------------------------------")

print(f"sum of 3 and 4 is {calculator.add(3,4)}")
print(f"difference of 3 from 4 is {calculator.sub(4,3)}")
print(f" 9 by 3 is {calculator.div(9,3)}")
