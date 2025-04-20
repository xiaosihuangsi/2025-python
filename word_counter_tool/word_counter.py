def main():
    filename = input("Enter the filename to count words: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        print(f"The file '{filename}' contains {len(words)} words.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode the file '{filename}'. Please check the encoding.")
