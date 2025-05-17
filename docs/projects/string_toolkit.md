# String Toolkit

The **String Toolkit** allows users to interactively explore string content through analysis, slicing, repetition, and character inspection. It helps reinforce key Python string concepts like indexing, slicing, type checking, and input validation.

---

## How to Use

When launched, the tool will:

1. Ask for a text input from the user.
2. Analyze the string:
   - Show the first and last characters.
   - Show the length of the string.
   - Repeat the string multiple times.
3. Ask for a substring range and extract it if valid.
4. Count vowels and identify character types (letters, digits, alphanumerics, special characters).

---

## Example

### Input
```bash
Enter a text: Python3.10!
How many times to repeat the text? (default 3): 2
Enter start index for substring (default 1): 1
Enter end index for substring (default 5): 5
```
### Output
```bash
String Analysis:
First character: P
Last character: !
Length of the text: 10
Text repeated 2 times: Python3.10!Python3.10!
Substring from index 1 to 5: ytho
Vowel count (a, e, i, o, u): 1
The text contains special characters.
```

## File Location
Path: `string_toolkit_tool/string_toolkit.py`