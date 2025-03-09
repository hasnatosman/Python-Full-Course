# python calculator 

num1= float(input("Enter the 1st number: "))
num2= float(input("Enter the 2nd number: "))

operator = input("Enter an operator (+ - * /) : ")

if operator == "+":
    result = num1 + num2
    print(f"The result is : {round(result,2)}")

if operator == "-":
    result = num1 - num2
    print(f"The result is : {round(result,2)}")

if operator == "*":
    result = num1 * num2
    print(f"The result is : {round(result,2)}")

if operator == "/":
    result = num1 / num2
    print(f"The result is : {round(result,2)}")
else:
    print(f"Your entered a invalid operator!")