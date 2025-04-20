from word_counter_tool.word_counter import main as word_counter_main
from calculator_tool.calculator import main as calculator_main
from string_toolkit_tool.string_toolkit import main as string_toolkit_main
from list_organizer_tool.list_organizer import main as list_organizer_main

def main():
    while True:
        print("\n✨ Welcome to the Python Tool Hub! ✨")
        print("-----------------------------------")
        print("Choose a tool:")
        print("1. Word Counter")
        print("2. Calculator")
        print("3. String Toolkit")
        print("4. List Organizer")
        print("5. Exit")
        print("-----------------------------------")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            word_counter_main()
        elif choice == '2':
            calculator_main()
        elif choice == '3':
            string_toolkit_main()
        elif choice == '4':
            list_organizer_main()
        elif choice == '5':
            print("\n👋 Goodbye! See you next time!")
            break
        else:
            print("\n❗ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
