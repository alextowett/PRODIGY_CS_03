def encrypt(text, shift):
    result = ""

    # Traverse through the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    
    while True:
        choice = input("\nDo you want to (e)ncrypt, (d)ecrypt or (q)uit? ").lower()
        
        if choice == 'e':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")

        elif choice == 'd':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

        elif choice == 'q':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
