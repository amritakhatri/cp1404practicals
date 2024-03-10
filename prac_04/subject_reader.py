"""
CP1404/CP5632 Practical
Data file -> lists program
CP1401,Ada Lovelace,192
CP1404,Alan Turing,98
CP4321,Bill Gates,676
CP1234,Steve Jobs,123
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        subject_data.append(parts)
    input_file.close()
    return subject_data


def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


if __name__ == "__main__":
    main()
