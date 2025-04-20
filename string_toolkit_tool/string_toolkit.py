def main():
    text = input("Enter a text: ")

    print("\nString Analysis:")
    print("First character:", text[0] if text else "Empty string")
    print("Last character:", text[-1] if text else "Empty string")
    print("Length of the text:", len(text))
    print("Text repeated 3 times:", text * 3)
    print("Substring from index 1 to 4:", text[1:5] if len(text) >= 5 else "Text too short")

if __name__ == "__main__":
    main()
