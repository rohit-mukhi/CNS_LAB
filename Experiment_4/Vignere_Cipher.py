def vigenere_cipher(text, key, mode='encrypt'):
    key = key.upper()
    modified_key = ""
    result = ""
    key_idx = 0
    for char in text:
        if char.isalpha():
            k_char = key[key_idx % len(key)]
            modified_key += k_char
            shift = ord(k_char) - ord('A')
            if mode == 'decrypt':
                shift = -shift
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
            key_idx += 1
        else:
            result += char
            modified_key += " "
    return result, modified_key

loop = 'y'

while loop == 'y':
    choice = int(input("Enter 1 to encrypt or 2 to decrypt: "))
    if choice == 1:
        message = input("Enter message: ")
        key = input("Enter key: ")
        cipher, key_used = vigenere_cipher(message, key, mode='encrypt')
        print("Original message: ", message)
        print("Key used: ", key_used)
        print("Cipher text: ", cipher)
    else:
        cipher = input("Enter cipher text: ")
        key = input("Enter key: ")
        message, key_used = vigenere_cipher(cipher, key, mode='decrypt')
        print("Cipher text: ", cipher)
        print("Key used: ", key_used)
        print("Message: ", message)
    loop = input("Do you want to continue? [y/n]: ")
    if loop == 'y' or loop == 'n':
        continue
    else:
        print("Invalid choice!")
        break
print("Thank you, have a nice day!")
