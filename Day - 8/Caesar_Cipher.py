# Caesar Cipher

print('''
  ____                              ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   
''')


def caesar_cipher(text, shift):
    plain_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new = position + shift
            else:
                new = position - shift
            new_letter = alphabet[new]
            plain_text += new_letter
        else:
            plain_text += letter
    print(plain_text.capitalize())


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice = input("Type yes to start: ")
while choice != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar_cipher(text, shift)
    choice = input("To continue type yes, if you want to end type no: ")
if choice == "no":
    print("\nGood Bye!")
