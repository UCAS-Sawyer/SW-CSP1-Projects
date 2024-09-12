# Sawyer Wood, for the average grade skillpractice.

class1 = float(input("What is the grade for your first period(Not a letter grade please)?: "))
class2 = float(input("What is the grade for your second period?: "))
class3 = float(input("What is the grade for your third period?: "))
Advisory = float(input("What is the grade for Advisory?: "))
class6 = float(input("What is the grade for your sixth period?: "))
class7 = float(input("What is the grade for your seventh period?: "))
class8 = float(input("What is the grade for your eighth period?: "))

GradesCombined = class1 + class2 + class3 + Advisory + class6 + class7 + class8
AverageGrade = GradesCombined/7
AverageGrade = round(AverageGrade, 2)
print("Your average grade is", AverageGrade, "%")