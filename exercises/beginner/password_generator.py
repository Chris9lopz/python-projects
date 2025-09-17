"""
Your task for today is to create a secure password generator in Python
that creates strong passwords based on user preferences.
This project strengthens your ability to work with strings,
random generation, and user input validation.

"""
# Import only choice option
from random import choice

# Get data for creates password
lower_data = [chr(x)for x in range(ord('a'), ord('z') + 1)]
upper_data = [chr(x)for x in range(ord('A'), ord('Z') + 1)]
number_data = [chr(x)for x in range(ord('0'), ord('9') + 1)]
special_chr_data = ['!', '@', '#', '$', '%', '^', '&', '*']

final_data = []

# Ask user password length
print("=== Password Generator ===")
password_len = int(input("Enter password length (minumum 8): "))

# Ask should include lowercase, uppercase, numbers, special caracters
has_lowercase = input("Include lowercase letters? (y/n): ")
has_uppercase = input("Include uppercase letters? (y/n): ")
has_numbers = input("Include numbers? (y/n):")
has_special_char = input("Include special characters? (y/n): ")

# Selecting data regarding with decision
responses = [has_lowercase, has_uppercase, has_numbers, has_special_char]
data_sets = [lower_data, upper_data, number_data, special_chr_data]

total_yes_responses = 0

for response, data_set in zip(responses, data_sets):
    if response == 'y':
        final_data.extend(data_set)
        total_yes_responses += 1

# Creating password according with final_data decision
password = [choice(final_data) for x in range(password_len)]

# Print password generated
print(f"\nGenerated Password: {''.join(password)}")
print(f"Character types used: {total_yes_responses}/4")
# Add password strength scoring (weak/medium/strong)
