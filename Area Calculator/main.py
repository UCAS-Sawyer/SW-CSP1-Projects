#Sawyer Wood, Raid Area Calculator

shape = input("What shape do you want to calculate?(Square, Rectangle, Triangle, Circle, Trapezoid): ")
shape = shape.lower()

if shape in ["square", "s"]:
    width = int(input("What is the width of the object?: "))   
    area = width **2
    print("The area of the square is", area, "units squared.")

if shape in ["rectangle", "r"]:
    hight = int(input("What is the hight of the object?: "))
    width = int(input("What is the width of the object?: "))   
    area = hight * width
    print("The area of the rectangle is", area, "units squared.")

if shape in ["triangle", "tri"]:
    hight = int(input("What is the hight of the object?: "))
    width = int(input("What is the width of the object?: "))   
    area = float((hight * width)/2)
    print("The area of the triangle is", area, "units squared.")

if shape in ["circle", "c"]:
    radius = int(input("What is the radius of the object?: "))
    area = (radius ** 2) * 3.14
    print("The area of the circle is", area, "units squared.")

if shape in ["trapezoid", "tra"]:
    hight = int(input("What is the hight of the object?: "))
    widtha = int(input("What is the width A of the object?: "))   
    widthb = int(input("What is the width B of the object?: "))  
    area = ((widtha + widthb)/2) * hight
    print("The area of the trapezoid is", area, "units squared.")