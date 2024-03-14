# Dictionary of colour names and their hexadecimal codes
COLOUR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

# Program loop
colour_name = input("Enter a colour name (or press Enter to exit): ").upper()
while colour_name:
    # Lookup colour code and print result
    colour_code = COLOUR_CODES.get(colour_name)
    if colour_code is not None:
        print(f"The hexadecimal code for {colour_name} is {colour_code}")
    else:
        print("Invalid colour name")

    # User input for the next colour name
    colour_name = input("Enter a colour name (or press Enter to exit): ").upper()
