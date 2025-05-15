def main():
    print("🛑 Pass Statement Demo\n")

    print("1. While True with pass (Press Ctrl+C to interrupt)")
    print("2. Placeholder function")
    print("3. Empty class definition")
    choice = input("Choose demo (1/2/3): ")

    if choice == "1":
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("\n👋 Interrupted by user.")
    elif choice == "2":
        def placeholder():
            pass
        print("Function defined with pass. Now calling it...")
        placeholder()
        print("✅ Nothing happened, but it's syntactically correct.")
    elif choice == "3":
        class Empty:
            pass
        e = Empty()
        print(f"✅ Created an empty class: {e}")
    else:
        print("❌ Invalid choice.")
