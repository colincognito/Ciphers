# The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher,
# whose increment is determined by the corresponding letter of another text, the key.

# How It Works:
#   Prompts the user to choose encryption or decryption and then to enter a message and a key
#   Processes the message accordingly and outputs the result.
#   Preserves spaces,numbers, and special characters


def vigenere_cipher(text, key, mode='encrypt'):
    """
    Encrypts or decrypts a message using the Vigenère Cipher.

    :param text: The message to process.
    :param key: The encryption/decryption key.
    :param mode: 'encrypt' or 'decrypt'.
    :return: The processed message.
    """
    text = text.upper()
    key = key.upper()
    # Repeat key to match text length
    key = (key * (len(text) // len(key) + 1))[:len(text)]

    result = []

    for i in range(len(text)):
        if text[i].isalpha():  # Only process letters
            shift = ord(key[i]) - ord('A')
            if mode == 'encrypt':
                new_char = chr(
                    (ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                new_char = chr(
                    (ord(text[i]) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(text[i])  # Preserve non-alphabet characters

    return ''.join(result)


# Interactive Input with File Option
mode = input(
    "Enter 'e' to encrypt a message or 'd' to decrypt a message: ").strip().lower()
# Map e/d to full terms
mode = 'encrypt' if mode == 'e' else 'decrypt' if mode == 'd' else None

if mode is None:
    print("Invalid mode. Please enter either 'e' or 'd'.")
    exit()

file_option = input(
    "Enter 'file' to read from a text file, or 'man'ual to type the message: ").strip().lower()

if file_option == 'file':
    file_path = input("Enter the text file path: ").strip().strip(
        '"')  # Removes extra quotes
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            message = file.read().strip()
    except FileNotFoundError:
        print("Error: File not found.")
        exit()
else:
    message = input("Enter the message: ").strip()

key = input("Enter the key: ").strip()

if mode in ['encrypt', 'decrypt']:
    processed_message = vigenere_cipher(message, key, mode)
    print(f"Processed message ({mode}): {processed_message}")
else:
    print("Invalid mode. Please enter 'e' or 'd'.")

# This process can be done multiple times with multiple keys for further encryption
