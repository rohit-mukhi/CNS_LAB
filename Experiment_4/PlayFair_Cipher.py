import re

def create_matrix(key):
    
    key = key.upper().replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    seen = set()
    
    
    for char in key + alphabet:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)g j, 
            x
            
    return [matrix[i:i+5] for i in range(0, 25, 5)]

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
    return [prepared[i:i+2] for i in range(0, len(prepared), 2)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def playfair(text, key, mode='encrypt'):
    matrix = create_matrix(key)
    pairs = prepare_text(text) if mode == 'encrypt' else [text[i:i+2] for i in range(0, len(text), 2)]
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


key = "MONARCHY"
message = "INSTRUMENTS"

encrypted = playfair(message, key, mode='encrypt')
decrypted = playfair(encrypted, key, mode='decrypt')

print(f"Key: {key}")
print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
