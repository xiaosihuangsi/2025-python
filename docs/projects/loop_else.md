# Loop-Else Prime Checker

The **Loop-Else Prime Checker** demonstrates how Python's `else` clause on a `for` loop can be used to detect **prime numbers**.

This approach is particularly elegant because the `else` block only executes **if the loop completes without hitting a `break`**—a behavior that's often underutilized but powerful for control flow logic.

---

## How to Use

1. Run the tool.
2. It will check numbers from `2` to `9`:
   - If a number is divisible by another, it prints the multiplication.
   - If no divisors are found, it prints that the number is prime.
3. Observe when the `else` clause runs (i.e., when no `break` occurs).

---

## Example

```text
🔎 Loop + Else Demo (Prime Number Detector)
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

💡 Tip: The 'else' only runs if the loop did NOT hit a break.

## File Location
```text
loop_else_tool/loop_else.py
```