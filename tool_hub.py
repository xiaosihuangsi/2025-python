from word_counter_tool.word_counter import main as word_counter_main
from calculator_tool.calculator import main as calculator_main
from string_toolkit_tool.string_toolkit import main as string_toolkit_main
from list_organizer_tool.list_organizer import main as list_organizer_main

def main():
    print("Welcome to the Python Tool Hub!")
    print("Choose a tool:")
    print("1. Word Counter")
    print("2. Calculator")
    print("3. String Toolkit")
    print("4. List Organizer")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        word_counter_main()
    elif choice == '2':
        calculator_main()
    elif choice == '3':
        string_toolkit_main()
    elif choice == '4':
        list_organizer_main()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
