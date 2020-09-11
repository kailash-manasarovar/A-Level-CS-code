def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
       if char in alphabet:
            phraseLetters += char
    for char in alphabet:
        if char not in phrase:
            print(phraseLetters, alphabet)
            return False

    return True

phrase = input("Enter a phrase to check")
print(is_pangram(phrase))