# match_tool/match_tool.py

def match_main():
    print("🎯 Match Statement Demo")

    status = int(input("Enter HTTP status code (e.g., 200, 404): "))
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case 401 | 403:
            print("Not allowed")
        case _:
            print("Something's wrong with the internet")
