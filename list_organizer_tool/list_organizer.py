def main():
    user_input = input("Enter a list of numbers separated by commas: ")
    numbers = [int(num.strip()) for num in user_input.split(",")]

    print("\nYour list:", numbers)

    new_item = int(input("Enter a new number to append: "))
    numbers.append(new_item)
    print("Updated list:", numbers)

    start = int(input("Enter start index for slicing: "))
    end = int(input("Enter end index for slicing: "))
    print("Sliced list:", numbers[start:end])

    copied_list = numbers[:]
    print("Copied list:", copied_list)

if __name__ == "__main__":
    main()
