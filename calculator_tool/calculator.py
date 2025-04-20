def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", add(a, b))
    elif operator == '-':
        print("Result:", subtract(a, b))
    elif operator == '*':
        print("Result:", multiply(a, b))
    elif operator == '/':
        print("Result:", divide(a, b))
    else:
        print("Error: Invalid operator.")

if __name__ == "__main__":
    main()
