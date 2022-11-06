from art import logo

print(logo) # Print logo

# List of letter of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction): # Calling parameters
        empty_text = [] # Create a empty list
        for letter in text:
            if letter in alphabet:
                word = alphabet.index(letter) # Looking for each letter in alphabet to know it index
                if direction == 'encode': # Calling direction = encode
                    empty_text.append(alphabet[word + shift]) # Moves 5 positions to the right
                elif direction == 'decode': # Calling direction = decode
                    empty_text.append(alphabet[word - shift]) # Moves 5 positions to the left
            else:
                empty_text.append(letter)

        new_word = ''.join(empty_text) # List to Str

        if direction == 'encode':
            print(f"The encode text is {new_word}") # Output message default
        else:
            print(f"The dencode text is {new_word}") # Output message default

end_program = False # Flag to finish the program

while not end_program: 
    # Inputs 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction) # Calling the function

    restart = input('Do you want to restart caesar cipher program? ').lower() # Ask if the user want to restart
    
    if restart == 'no': # If answer is no the program will restart
        print('Goodbye')
        end_program = True
