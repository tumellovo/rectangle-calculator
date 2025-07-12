import calculations

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = calculations.area(length, width)
perimeter = calculations.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")