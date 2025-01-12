def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length is between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are alphabetic
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters
    for c in s:
        if c in [' ', '?', '.', ',', '!']:
            return False

    # Find the index where numbers start, if any
    i = 0
    while i < len(s) and s[i].isalpha():
        i += 1

    # Ensure all characters after the first non-alpha are digits
    if i < len(s):
        for j in range(i, len(s)):
            if not s[j].isdigit():
                return False
            # Ensure there's no leading zero in the numeric part
            if s[j] == '0' and j == i:
                return False

    return True

if __name__ == "__main__":
    main()
