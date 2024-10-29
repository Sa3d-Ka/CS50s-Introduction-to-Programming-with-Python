def main():
    msg = input()
    result = convert(msg)
    print(result)


def convert(msg):
    msg1 = msg.replace(":)", "🙂").replace(":(", "🙁")

    return msg1


main()