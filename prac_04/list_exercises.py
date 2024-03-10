# Initialise an empty list to store numbers
numbers = []

# Prompt the user for 5 numbers and append them to the list
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

# Output information about the numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

# List of authorised usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
user_input = input("Enter your username: ")

# Check if the entered username is in the list of authorised users
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
