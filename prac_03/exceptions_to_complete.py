is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True to exit the loop when a valid integer is entered
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)