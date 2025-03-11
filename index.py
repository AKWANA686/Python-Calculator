num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
operation = input("Operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/" and num2 != 0:
    print(num1 / num2)
else:
    print("Invalid operation")