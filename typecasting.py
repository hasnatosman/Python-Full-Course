# typecasting: the process of converting a variable from one data type to another

name = "Imran"
age = 25
gpa = 3.5
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

name = bool(name)
print(name)

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

age = str(age)
print(age)

age += "10"
print(age)