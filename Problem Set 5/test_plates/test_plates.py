from plates import is_valid

def main():
    test_invalid()
    test_valid()

def test_invalid():
    # Too short
    assert is_valid("C") == False
    # Too long
    assert is_valid("OUTATIME") == False
    # Starts with numbers
    assert is_valid("12CS") == False
    # Contains special characters
    assert is_valid("PI3.14") == False
    # Numbers in the middle
    assert is_valid("CS50P") == False
    # Leading zero
    assert is_valid("CS05") == False
    # Lowercase and leading zero
    assert is_valid("50") == False

def test_valid():
    # Valid plate
    assert is_valid("CS50") == True
    # Valid plate with all letters
    assert is_valid("HELLO") == True
    # Valid plate with numbers at the end
    assert is_valid("AAA222") == True

if __name__ == "__main__":
    main()