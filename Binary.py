def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return ''.join(chr(int(b, 2)) for b in binary.split())

def process_choice():
    choice = input("Do you want to convert text to binary (1) or revert binary to text (2)? Enter 1 or 2: ")
    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return process_choice()

    source = input("Do you want to manually enter text (m) or read from a text file (f)? Enter m or f: ")
    if source not in ['m', 'f']:
        print("Invalid input. Please enter m or f.")
        return process_choice()

    if source == 'm':
        message = input("Enter your message: ")
    else:
        file_path = input("Enter the file path: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                message = file.read().strip()
        except FileNotFoundError:
            print("File not found. Try again.")
            return process_choice()

    if choice == '1':
        print("Binary Output:", text_to_binary(message))
    else:
        print("Text Output:", binary_to_text(message))

if __name__ == "__main__":
    process_choice()