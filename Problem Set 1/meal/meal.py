def main():
    time = input("What time is it? ")
    x = convert(time)
    if 7.00 <= x <= 8.00:
        print("breakfast time")
    elif 12.00 <= x <= 13.00:
        print("lunch time")
    elif 18.00 <= x <= 19.00:
        print("dinner time")



def convert(time):
    
    x, y = time.split(":")

    float_x = float(x)
    float_y = float(y) / 60

    float_time = float_x + float_y
    return float_time

if __name__ == "__main__":
    main()
