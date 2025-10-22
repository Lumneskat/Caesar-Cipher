def caesar():
    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    shift_amount = shift_amount % len(alphabet)

    if direction == "encode":
        encrypted_word = []

        for letter in original_text:

            if letter not in alphabet:
                encrypted_word.append(letter)
                continue

            letter_index = alphabet.index(letter)
            new_index = letter_index + shift_amount

            if new_index > len(alphabet) - 1:
                new_index = new_index - len(alphabet)

            encrypted_word.append(alphabet[new_index])

        print("".join(encrypted_word))

    elif direction == "decode":
        decrypted_word = []

        for letter in original_text:
            if letter not in alphabet:
                decrypted_word.append(letter)
                continue

            letter_index = alphabet.index(letter)
            new_index = letter_index - shift_amount

            if new_index < 0:
                new_index = len(alphabet) + new_index

            decrypted_word.append(alphabet[new_index])

        print("".join(decrypted_word))

    else:
        print("It's an INPUT ERROR 001, bitch!")


caesar()
