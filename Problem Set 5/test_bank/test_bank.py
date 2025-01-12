from bank import value

def main():
    test_hello()
    test_greeting_starts_with_h()
    test_other_greeting()
    

def test_hello():
    assert value("hello") == "$0"
    assert value(" hello  ") == "$0"

def test_greeting_starts_with_h():
    assert value(" hi") == "$20"
    assert value("How you doing?") == "$20"

def test_other_greeting():
    assert value("What's happening?") == "$100"

if __name__ == "__main__":
    main()