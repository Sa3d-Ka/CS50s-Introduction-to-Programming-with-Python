import emoji

msg = input("Input: ")

print(f"Output: {emoji.emojize(msg, language='alias')}")
