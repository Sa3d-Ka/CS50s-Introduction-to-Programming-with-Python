def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    if "hello" in greeting.lower().strip() :
        return 0
    elif greeting.lower().strip().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

