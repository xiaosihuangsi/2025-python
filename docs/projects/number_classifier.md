# Number Classifier Tool

The **Number Classifier Tool** prompts the user for an integer and classifies the number as:

- Negative → reported as changed to zero  
- Zero  
- One (displayed as "Single")  
- Greater than one (displayed as "More")

This is a great beginner exercise for conditional logic in Python.

---

## How to Use

1. Run the tool.
2. Enter any integer (e.g., -5, 0, 1, 42).
3. Based on the value, the tool prints one of the following:

 - `"Negative changed to zero"`
 - `"Zero"`
 - `"Single"`
 - `"More"`

---

## Example

```bash
Please enter an integer: -3
Negative changed to zero

Please enter an integer: 0
Zero

Please enter an integer: 1
Single

Please enter an integer: 5
More
```

If a non-integer is entered, the tool prints:

```bash
❌ Invalid input! Please enter a number.
```

## File Location
```bash
Path: `number_classifier_tool/number_classifier.py`
```