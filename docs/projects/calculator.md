# Calculator Tool

The **Calculator Tool** performs basic arithmetic operations: addition, subtraction, multiplication, and division.   It’s ideal for beginners learning how to take user input and apply conditional logic to real-world calculations.

---

## How to Use

You can run this tool by executing the script directly or from the Python Tool Hub menu.

Follow the prompts:

1. Enter the first number  
2. Choose an operator (`+`, `-`, `*`, `/`)  
3. Enter the second number

The tool will then display the **result**.  
If an invalid operator is entered or division by zero occurs, an error message will be shown.

---

## Example

### Addition

```bash
$ python calculator.py
Enter first number: 12  
Enter operator (+, -, *, /): +  
Enter second number: 8  
```
Result: 20.0

### Division by Zero
```bash
$ python calculator.py
Enter first number: 10  
Enter operator (+, -, *, /): /  
Enter second number: 0  
```
Result: Error: Cannot divide by zero.

## File Location

```bash
Path: calculator_tool/calculator.py
```