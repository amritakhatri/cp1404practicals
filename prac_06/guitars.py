
from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    # Test data (comment out when not testing)
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Collect user input
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")

    # Print guitar details
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i:<2}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:>10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
