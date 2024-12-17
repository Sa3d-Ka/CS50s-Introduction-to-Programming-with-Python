import inflect

names = []

while True:
    try:
        msg= input("Name: ").strip().capitalize()
        names.append(msg)
    except EOFError:
        break
p = inflect.engine()
print("\nAdieu, adieu, to", p.join(names))
   