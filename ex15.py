# Importing the argv part of the sys module so the script can take CLI input
from sys import argv

# Assigning var's from CLI input following script name
script, filename = argv

# Opening the file from CLI and assigning to txt var.
txt = open(filename)

#Printing file name by using f and {} from var
print(f"Here's your file {filename}:")
#printing contents of file to screen
print(txt.read())

# Prompting user for a file name to print
print("Type the filename again:")
# Store file in prompt to 'file_again'
file_again = input("> ")

# Store open file in 'file_again' to 'txt_again'
txt_again = open(file_again)

# Print contents of 2nd text file to screen
print(txt_again.read())
