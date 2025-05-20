def list_loop_demo():
    words = input("Enter a list of words, separated by commas: ").split(',')
    print("\n📋 Word and Lengths:")
    for word in words:
        print(f"- {word.strip()} ({len(word.strip())} letters)")

def dict_loop_demo():
    users = {
        'Hans': 'active',
        'Éléonore': 'inactive',
        'Lulu': 'active'
    }
    print("\n👥 All users and statuses:")
    for user, status in users.items():
        print(f"- {user}: {status}")

    print("\n✅ Filtering active users:")
    for user, status in users.items():
        if status == 'active':
            print(f"- {user}")

def main():
    print("🎯 For Loop Practice Tool")
    print("1. List loop demo")
    print("2. Dictionary loop demo")
    
    choice = input("Choose demo (1/2): ")

    if choice == '1':
        list_loop_demo()
    elif choice == '2':
        dict_loop_demo()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
