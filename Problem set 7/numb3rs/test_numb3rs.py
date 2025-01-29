from numb3rs import validate


def test_validate():
    # Valid IPv4 addresses
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True

    # Invalid IPv4 addresses
    assert validate("512.512.512.512") == False  # Invalid octet (512 > 255)
    assert validate("1.2.3.1000") == False       # Invalid octet (1000 > 255)
    assert validate("256.255.255.255") == False  # Invalid first octet
    assert validate("64.128.256.512") == False   # Invalid third and fourth octets
    assert validate("8.8.8") == False            # Missing an octet
    assert validate("10.10.10.10.10") == False   # Five octets
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False  # IPv6 address
    assert validate("cat") == False              # Not an IP address
    assert validate("1.2.3.4.5") == False        # Extra octet
    assert validate("1..3.4") == False           # Missing octet
    assert validate("1.2.3.") == False           # Trailing dot
    assert validate(".1.2.3") == False           # Leading dot


if __name__ == "__main__":
    test_validate()