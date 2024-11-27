# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Wyatt Engelmann
# created: 11.21.24
# last update:  11.27.24
import os

# Alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode_text_file(filename, key):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
        # Encode the content using the shift_string function
        encoded_content = shift_string(content, key)
        if encoded_content is not None:
            # Write the encoded content back to the file
            with open(filename, 'w') as file:
                file.write(encoded_content)
            print(f"Encoded {filename} with key {key}")
        else:
            print(f"Failed to encode {filename} due to invalid key.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def shift_string(s, key):
    try:
        # Convert key to an integer
        key = int(key)
    except ValueError:
        print("Invalid key. Please enter a valid integer.")
        return None  # Return None if the key is invalid

    result = []
    for char in s:
        if char.isalpha():
            # Calculate the shift value
            shift = key % 26
            if char.islower():
                # Shift lowercase characters
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                # Shift uppercase characters
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return ''.join(result)  # Return the encoded string

def encode_message():
    # Get the string and key from the user
    string = input("Input the string you want to encode:\n")
    key = input("Input the number of letters you want to shift by:\n")
    # Encode the string using the shift_string function
    encoded_string = shift_string(string, key)
    if encoded_string is not None:
        print("Encoded message:", encoded_string)

def decode_unknown_key(filename):
    # Try decoding the file with all possible keys (1 to 26)
    for key in range(1, 27):
        try:
            encode_text_file(filename, -key)
        except Exception as e:
            print(f"An error occurred with key {-key}: {e}")

def main():
    while True:
        # Display the menu options
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: View File Contents.\n"
              f"[5]: Exit.")

        # Get the user's selection
        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            # List text files in the current directory
            files = os.listdir('.')
            text_files = [f for f in files if f.endswith('.txt')]

            print("Text files in the current directory:")
            for i, text_file in enumerate(text_files, start=1):
                print(f"[{i}]: {text_file}")

            try:
                # Get the user's choice of file to encode
                choice = int(input("Enter the number of the file you want to encode: ")) - 1
                if 0 <= choice < len(text_files):
                    filename = text_files[choice]
                    key = input("Enter the key for encoding: ")
                    encode_text_file(filename, key)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif selection == "3":
            # List text files in the current directory
            files = os.listdir('.')
            text_files = [f for f in files if f.endswith('.txt')]

            print("Text files in the current directory:")
            for i, text_file in enumerate(text_files, start=1):
                print(f"[{i}]: {text_file}")

            try:
                # Get the user's choice of file to decode
                choice = int(input("Enter the number of the file you want to decode: ")) - 1
                if 0 <= choice < len(text_files):
                    filename = text_files[choice]
                    key_input = input("Enter the key for encoding (or type 'NONE' to iterate over 26 keys): ")

                    if key_input.upper() == "NONE":
                        decode_unknown_key(filename)
                    else:
                        try:
                            key = int(key_input)
                            encode_text_file(filename, -key)
                        except ValueError:
                            print("Invalid key. Please enter a valid integer or 'NONE'.")
                        except Exception as e:
                            print(f"An error occurred: {e}")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
