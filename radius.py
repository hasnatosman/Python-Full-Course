import math
radius = float(input("Enter the value: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)


print(f"The circumference is: {round(circumference,2)}cm")
print(f"The area is: {round(area,2)}cm^2")