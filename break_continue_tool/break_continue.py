def main():
    print("🔁 Break & Continue Practice")
    print("1. Find first divisor using break")
    print("2. Filter even/odd using continue")
    choice = input("Choose a demo (1/2): ")

    if choice == "1":
        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    print(f"{n} equals {x} * {n // x}")
                    break
            else:
                print(f"{n} is a prime number")
    elif choice == "2":
        for num in range(2, 10):
            if num % 2 == 0:
                print(f"Found an even number: {num}")
                continue
            print(f"Found an odd number: {num}")
    else:
        print("❌ Invalid choice.")
