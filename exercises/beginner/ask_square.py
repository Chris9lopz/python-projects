# Repeatedly asks the user to enter a number and prints its square

# Loop through the input question
while True:
    # Retrieve the information of the number
    input_user = input("Enter a number (or 'q' to quit): ")
    # Checks if is a q for quit else show the square of the number
    if input_user.lower() == 'q':
        break
    else:
        print(f"Square: {int(input_user) * int(input_user)}")
