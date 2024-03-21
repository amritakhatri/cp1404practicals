"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

state_dict = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(state_dict)

while True:
    state_code = input("Enter short state (or press Enter to exit): ").upper()
    if not state_code:
        break

    try:
        state_name = state_dict[state_code]
        print(f"{state_code} is {state_name}")
    except Exception as e:
        print(f"Error: {e}")
        print("Invalid short state")

# Loop to print all states and names neatly
for code, name in state_dict.items():
    print(f"{code} is {name}")
