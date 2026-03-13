def encrypt(message, key):

        cipher = ""

        for letter in message:

                if 65 <= ord(letter) <= 90:

                        result = chr((ord(letter) + key - 65) % 26 + 65)

                        cipher = cipher + result

                elif 97 <= ord(letter) <=  122:

                        result = chr((ord(letter) + key - 97) % 26 + 97)

                        cipher = cipher + result

                elif letter == " ":

                        cipher = cipher + " "

        return cipher


def decrypt(message, key):

        cipher = ""


        for letter in message:

                if 65 <= ord(letter) <= 90:

                        result = chr((ord(letter) - key + 65) % 26 - 65)

                        cipher = cipher + result

                elif 97 <= ord(letter) <=  122:

                        result = chr((ord(letter) - key + 97) % 26 - 97)

                        cipher = cipher + result

                elif letter == " ":

                        cipher = cipher + " "

        return cipher



choice = int(input("Enter 1 to encrypt, 2 to decrypt: "))


if choice == 1:

        message = input("Enter message: ")

        key = int(input("Enter key: "))

        cipher = encrypt(message, key)

elif choice == 2:

        message = input("Enter cipher: ")

        key = int(input("Enter key: "))

        cipher = decrypt(message, key)

else:

print("Invalid choice")


print("Encrypted text: ", cipher) 
