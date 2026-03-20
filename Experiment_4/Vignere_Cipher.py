def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            
            start = ord('A') if char.isupper() else ord('a')
            
            
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            if mode == 'encrypt':
               
                new_char = chr(start + (ord(char) - start + shift) % 26)
            else:
               
                new_char = chr(start + (ord(char) - start - shift) % 26)
                
            result += new_char
            key_index += 1
        else:
            
            result += char
            
    return result


message = "Hello World"
keyword = "PYTHON"

encrypted = vigenere_cipher(message, keyword, mode='encrypt')
decrypted = vigenere_cipher(encrypted, keyword, mode='decrypt')

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
