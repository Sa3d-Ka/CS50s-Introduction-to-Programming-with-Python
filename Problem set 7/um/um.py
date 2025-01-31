import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    x = re.findall(pattern, s, flags=re.IGNORECASE)
    return len(x)


if __name__ == "__main__":
    main()