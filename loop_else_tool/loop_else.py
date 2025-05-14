
def main():
    print("🔎 Loop + Else Demo (Prime Number Detector)")
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} equals {x} * {n // x}")
                break
        else:
            print(f"{n} is a prime number")

    print("\n💡 Tip: The 'else' only runs if the loop did NOT hit a break.")
