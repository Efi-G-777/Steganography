def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def caesar_cipher_mult(text, key):
    result = ""
    shift = 0
    for char in text:
        if char.isalpha():
            shift_amount = key[shift] % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
            shift = (shift + 1) % (len(key) - 1)
        else:
            result += char
    return result

print(caesar_cipher_mult("Hello world", (1, 2, 3)))

