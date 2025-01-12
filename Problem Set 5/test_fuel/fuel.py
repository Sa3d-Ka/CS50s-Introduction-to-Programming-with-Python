def main():
    fuel = input("Fraction: ")
    percentage = convert(fuel)
    print(gauge(percentage))


def convert(fraction):
    while True:   
        try:
            x, y = fraction.split("/")
            new_x = int(x)
            new_y = int(y)
            f = new_x / new_y
            if f <= 1:
                p = round(f*100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage == 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
