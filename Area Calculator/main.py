#Sawyer Wood, Raid Area Calculator

shape = input("What shape do you want to calculate?(Square, Rectangle, Triangle, Circle, Trapezoid): ")
shape = shape.lower()

def rectangle_area(name):
    if name == "square":
        width = int(input("What is the width of the object?: "))
        area = width ** 2

    elif name == "rectangle":
        width = int(input("What is the width of the object?: "))  
        hight = int(input("What is the hight of the object?: ")) 
        area = width * hight

    print("The area of the ", name, " is", area, "units squared.")

def triangle_area():
    hight = int(input("What is the hight of the object?: "))
    width = int(input("What is the width of the object?: "))   
    area = float((hight * width)/2)
    print("The area of the triangle is", area, "units squared.")

def circle_area():
    radius = int(input("What is the radius of the object?: "))
    area = (radius ** 2) * 3.14
    print("The area of the circle is", area, "units squared.")

def trapezoid_area():
    hight = int(input("What is the hight of the object?: "))
    widtha = int(input("What is the width A of the object?: "))   
    widthb = int(input("What is the width B of the object?: "))  
    area = ((widtha + widthb)/2) * hight
    print("The area of the trapezoid is", area, "units squared.")

if shape in ["square", "s"]:
    rectangle_area("square")

if shape in ["rectangle", "r"]:
    rectangle_area("rectangle")

if shape in ["triangle", "tri"]:
    triangle_area()

if shape in ["circle", "c"]:
    circle_area()

if shape in ["trapezoid", "tra"]:
    trapezoid_area()