'''def greet(name):
    print(f"Hello, {name}!")

greet("Anand")
greet("Ravi")'''


'''def add(a, b):
    print(a + b)

add(10, 20)
add(100, 200)'''

'''def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))'''



def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
            return

    else:
        print("Invalid operator")
        return

    print(f"Result: {result}")

calculator()