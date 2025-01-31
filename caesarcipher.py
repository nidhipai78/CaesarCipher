#Caesar Cipher

#encryption
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start=ord('a')
            shifted_pos = (ord(char) - start + shift) % 26
            shifted_char = chr(shifted_pos + start)
            result += shifted_char
        else:
            result += char
    return result

#decryption
def caesar_decipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
             if char.isupper():
                start = ord('A')
             else:
                start=ord('a')
             shifted_pos = (ord(char) - start - shift) % 26
             shifted_char = chr(shifted_pos + start)
             result += shifted_char
        else:
            result += char
    return result

txt=input("Enter string ")
shift_value = 3

# Encryption
encrypted = caesar_cipher(txt, shift_value)
print("Encrypted:", encrypted)

# Decryption
decrypted = caesar_decipher(encrypted, shift_value)
print("Decrypted:", decrypted)
