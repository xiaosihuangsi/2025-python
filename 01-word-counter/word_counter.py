import sys

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        print(f"The file '{filename}' contains {len(words)} words.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode the file '{filename}'. Please check the encoding.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <filename>")
    else:
        count_words_in_file(sys.argv[1])
