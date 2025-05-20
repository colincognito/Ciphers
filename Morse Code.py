import os

# Morse Code Dictionary
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

# Reverse dictionary for decoding
MORSE_REVERSE_DICT = {v: k for k, v in MORSE_DICT.items()}

def text_to_morse(text):
    return ' '.join(MORSE_DICT.get(char.upper(), '') for char in text)

def morse_to_text(morse):
    return ''.join(MORSE_REVERSE_DICT.get(code, '') for code in morse.split())

def process_message(choice):
    while True:
        message = input("Enter your message: ").strip()
        break

    if choice == 'C':
        print("Morse Code:", text_to_morse(message))
    elif choice == 'R':
        print("Converted Text:", morse_to_text(message))
    else:
        print("Invalid choice. Please restart the program.")

def main():
    while True:
        choice = input("Do you want to convert to Morse code (C) or revert from Morse code (R)? ").strip().upper()
        if choice in {'C', 'R'}:
            process_message(choice)
            break
        else:
            print("Invalid choice. Please enter 'C' or 'R'.")

if __name__ == "__main__":
    main()