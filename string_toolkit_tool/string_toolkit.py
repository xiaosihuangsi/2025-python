def analyze_text(text):
    """Analyze and print various properties of the text."""
    print("\n🔍 String Analysis:")
    print(f"- First character: {text[0]}")
    print(f"- Last character: {text[-1]}")
    print(f"- Length of the text: {len(text)}")

    repeat_times = get_repeat_times()
    print(f"- Text repeated {repeat_times} times: {text * repeat_times}")

    get_substring(text)
    analyze_characters(text)

def get_repeat_times():
    """Ask user for repeat times."""
    try:
        repeat_times = int(input("How many times to repeat the text? (default 3): ") or 3)
        return repeat_times if repeat_times > 0 else 3
    except ValueError:
        return 3

def get_substring(text):
    """Extract and print a substring based on user input."""
    try:
        start = int(input("Enter start index for substring (default 1): ") or 1)
        end = int(input("Enter end index for substring (default 5): ") or 5)
        if 0 <= start < end <= len(text):
            print(f"- Substring from index {start} to {end}: {text[start:end]}")
        else:
            print("- Invalid substring indices. Skipping substring extraction.")
    except ValueError:
        print("- Invalid input for indices. Skipping substring extraction.")

def analyze_characters(text):
    """Analyze character types and vowel counts."""
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)
    print(f"- Vowel count (a, e, i, o, u): {vowel_count}")

    if text.isalpha():
        print("- The text contains only letters.")
    elif text.isdigit():
        print("- The text contains only digits.")
    elif text.isalnum():
        print("- The text contains both letters and numbers.")
    else:
        print("- The text contains special characters.")

def main():
    text = input("Enter a text: ").strip()
    if text:
        analyze_text(text)
    else:
        print("\n❗ Error: You entered an empty string.")

if __name__ == "__main__":
    main()
