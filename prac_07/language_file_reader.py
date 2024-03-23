"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        # Add handling for the new Pointer Arithmetic field
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), parts[4] == "Yes")
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)

main()
