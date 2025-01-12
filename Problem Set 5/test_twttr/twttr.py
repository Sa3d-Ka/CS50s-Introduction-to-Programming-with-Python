def main():
    word = input("Input: ")
    print("Output: ", end="")
    word_without_vowel = shorten(word)
    print(f'{word_without_vowel}')
    


def shorten(word):
    word_without_vowel = ''
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
           word_without_vowel += letter
    return word_without_vowel
           

if __name__ == "__main__":
    main()