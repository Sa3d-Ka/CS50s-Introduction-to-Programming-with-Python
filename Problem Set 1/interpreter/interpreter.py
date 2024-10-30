txt = input("Expression: ")

x, y, z = txt.split(" ")

float_x = float(x)
float_z = float(z)

if y == "+":
    print(float_x + float_z)
elif y == "-":
    print(float_x - float_z)
elif y == "/" and float_z != 0:
    print(float_x / float_z)
elif y == "/" and float_z == 0:
    print("error division by zero.")
elif y == "*":
    print(float_x * float_z)
else:
    print("Invalid operation")

