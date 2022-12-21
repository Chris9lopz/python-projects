# Exercise identify the extension of a file given by the user

def identify_extension(file):
    position_dot = file.find('.')
    return file[position_dot:]


file_name = input('Please enter the name of the file with its respective extension: ')

extension = identify_extension(file_name)

print(f'The extension file is: {extension}')

