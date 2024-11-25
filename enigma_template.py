# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: YOUR_NAME_HERE
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY

import random
import os

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
def encode_text_file(filename, key):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        encoded_content = shift_string(content, key)
        if encoded_content is not None:
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
        key = int(key)  # Convert key to an integer
    except ValueError:
        print("Invalid key. Please enter a valid integer.")
        return None  # Return None if the key is invalid

    result = []
    for char in s:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)  # Return the encoded string

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    string = input("Input the string you want to encode:\n")
    key = input("Input the number of letters you want to shift by:\n")
    encoded_string = shift_string(string, key)
    if encoded_string is not None:
        print("Encoded message:", encoded_string)

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    key = int(input("Define what value you want to shift by:"))
    # List all files in the current directory
    files = os.listdir('.')
    text_files = [f for f in files if f.endswith('.txt')]

    # Print out all text files
    print("Text files in the current directory:")
    for text_file in text_files:
        print(text_file)

    # Encode the contents of each text file
    for text_file in text_files:
        with open(text_file, 'r') as file:
            content = file.read()
        encoded_content = shift_string(content, key)
        if encoded_content is not None:
            with open(text_file, 'w') as file:
                file.write(encoded_content)
            print(f"Encoded {text_file} with key {key}")
            print("Encoded content:")
            print(encoded_content)  # Print the encoded content
        else:
            print(f"Failed to encode {text_file} due to invalid key.")

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            files = os.listdir('.')
            text_files = [f for f in files if f.endswith('.txt')]

            # Print out all text files
            print("Text files in the current directory:")
            for i, text_file in enumerate(text_files, start=1):
                print(f"[{i}]: {text_file}")

            # Get user's choice of file to encode
            try:
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
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()