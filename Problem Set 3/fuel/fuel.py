while True:
    fuel = input("Fraction: ")    
    try:
        x, y = fuel.split("/")
        new_x = int(x)
        new_y = int(y)
        f = new_x / new_y
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
        
p = f*100
if p == 100:
    print("F")
elif p <= 1:
    print("E")
else:
    print(f"{int(p)}%")
