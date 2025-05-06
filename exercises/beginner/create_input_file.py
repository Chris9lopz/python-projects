# Request an user input and save as a file

# Create file handler create file
with open("new_file.txt", "w") as file:
    # Loop three times to get sentences from the user
    for i in range(3):
        # Prompt the user to enter a sentence
        sentence = input(f"Enter sentence {i+1}: ")
        # Write the sentence to the file
        file.write(sentence + "\n")
        # If it's not the last sentence, add dash lines
        if i < 2:
            file.write("-----------\n")
