# number_classifier_tool/number_classifier.py

def main():
    try:
        x = int(input("Please enter an integer: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    if x < 0:
        print("Negative changed to zero")
    elif x == 0:
        print("Zero")
    elif x == 1:
        print("Single")
    else:
        print("More")
