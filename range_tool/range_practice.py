def main():
    print("\U0001F4CF Range Practice Tool\n")

    try:
        start = int(input("Start: "))
        end = int(input("End: "))
        step = int(input("Step: "))
    except ValueError:
        print("\n❌ Please enter valid integers for start, end, and step.")
        return

    if step == 0:
        print("\n⚠️ Step cannot be zero.")
        return

    r = list(range(start, end, step))
    print(f"\nGenerated sequence: {r}")
    print(f"Sum of values: {sum(r)}")
    print(f"Length: {len(r)}")

if __name__ == "__main__":
    main()
