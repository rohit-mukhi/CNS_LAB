import re

def create_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace('J', 'I')))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    chars = []
    seen = set()
    for char in key + alphabet:
        if char not in seen and char.isalpha():
            seen.add(char)
            chars.append(char)

    return [chars[i:i+5] for i in range(0, 25, 5)]

def display_matrix(matrix):
    print("\nPlayfair Matrix")
    for row in matrix:
        print("  ".join(row))
    print("\n")
def prepare_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper().replace('J', 'I'))
    prepared = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        prepared += char1
        if i + 1 < len(text):
            char2 = text[i+1]
            if char1 == char2:
                prepared += 'X'
            else:
                prepared += char2
                i += 1
        else:
            prepared += 'X'
        i += 1

    pairs = [prepared[i:i+2] for i in range(0, len(prepared), 2)]
    return pairs

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def playfair_logic(text, key, mode='encrypt'):
    matrix = create_matrix(key)
    display_matrix(matrix)

    if mode == 'encrypt':
        pairs = prepare_text(text)
        print(f"Digraphs (Pairs): {' '.join(pairs)}")
    else:
        pairs = [text[i:i+2] for i in range(0, len(text), 2)]
        print(f"Cipher Pairs: {' '.join(pairs)}")

    result = []
    shift = 1 if mode == 'encrypt' else -1

    for char1, char2 in pairs:
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        if r1 == r2:
            result.append(matrix[r1][(c1 + shift) % 5])
            result.append(matrix[r2][(c2 + shift) % 5])
        elif c1 == c2:
            result.append(matrix[(r1 + shift) % 5][c1])
            result.append(matrix[(r2 + shift) % 5][c2])
        else:
            result.append(matrix[r1][c2])
            result.append(matrix[r2][c1])
    return "".join(result)


choice = input("Choose (1) Encrypt or (2) Decrypt: ")
user_text = input("Enter text: ")
user_key = input("Enter Key: ")

if choice == '1':
    output = playfair_logic(user_text, user_key, mode='encrypt')
    print(f"\nFinal Ciphertext: {output}\n")
elif choice == '2':
    output = playfair_logic(user_text, user_key, mode='decrypt')
    print(f"\nFinal Decrypted Text: {output}\n")
else:
   print("Invalid choice!")
