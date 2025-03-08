# Script for communicating with an LLM via a 'book cypher' way.
# More info in further versions.
# .




import numpy as np

# Load "The Book" as a list of words
BOOK_TEXT = """
The quick brown fox, so light on its feet, Jumps over the lazy dog, swift yet discreet.
A wizard packs jugs, a box full of gold, Five dozen bottles, the tale retold.
Sphinx of black quartz, judging with might, Dizzy gophers dance in the pale moonlight.
Zealous nymphs bake, their cakes stacked high, While Oxford’s wizards make toads fly.
Numbers whisper, etched in stone, 0123456789 stand alone.
Symbols scattered in cryptic delight, !@#$%^&*()_+-=[]{}|;:'\",.<>?/ shine bright.
A vow is spoken, a puzzle is cast, Mixing the letters, ensuring they last.
Jumping wizards, boxing in line, Their rhythms encode a hidden sign.
The cipher hums where riddles hide, ABCDEFGHIJKLMNOPQRSTUVWXYZ abide.
Lower echoes, their shadows play, abcdefghijklmnopqrstuvwxyz lead the way.
The river of glyphs flows deep and wide, With symbols and numbers set to guide.
A puzzle of ink, a dance of the mind, Each fragment a secret for those who find.
Lurking in pages where silence sways, The whispers of code in delicate phrase.
A bridge between letters, a structured art, A spell that ensures the puzzle will start.
Between the lines, the echoes call, Figures and runes engraved on the wall.
0123456789 return again, Bound in the whispers of ink and pen.
A fox may leap, a dog may rest, But ciphers remain, a language possessed.
An alphabet forged, both shadowed and bright, A tale untold, yet hidden in sight.
Scribes and seekers, heed this verse, Unlock the book, for better or worse.
Letters and numbers, woven so tight, Keep them close, and read them right.
""".split("\n")  # Split into lines

# Convert The Book into a structured data format
BOOK_INDEX = []
for line_num, line in enumerate(BOOK_TEXT, start=1):
    words = line.split()
    word_positions = [[list(word) for word in words]]
    BOOK_INDEX.append(word_positions)

# Function to encode a message
def encode_message():
    message = input("Enter the message to encode: ")
    encoded = []
    for char in message:
        found = False
        for line_num, line in enumerate(BOOK_INDEX, start=1):
            for word_num, word in enumerate(line[0], start=1):
                for letter_num, letter in enumerate(word, start=1):
                    if letter.lower() == char.lower():
                        encoded.append(f"{line_num},{word_num},{letter_num}")
                        found = True
                        break
                if found:
                    break
            if found:
                break
    encoded_text = ", ".join(encoded)
    print(f"\nEncoded Message: {encoded_text}\n")
    return encoded_text

# Function to decode a cipher
def decode_cipher():
    cipher_text = input("Enter the cipher to decode: ")
    decoded = []
    positions = cipher_text.split(", ")
    for pos in positions:
        try:
            line, word, letter = map(int, pos.split(','))
            decoded.append(BOOK_INDEX[line-1][0][word-1][letter-1])
        except:
            decoded.append('?')  # Handle errors gracefully
    decoded_text = "".join(decoded)
    print(f"\nDecoded Message: {decoded_text}\n")
    return decoded_text

# User-friendly menu for encoding and decoding
def main():
    while True:
        print("\n===== Book Cipher Tool =====")
        print("1. Encode a message")
        print("2. Decode a cipher")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            encode_message()
        elif choice == '2':
            decode_cipher()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
