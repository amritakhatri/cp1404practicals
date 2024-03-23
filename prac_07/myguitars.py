
from guitar import Guitar

def load_guitars(filename):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display information about guitars in the list."""
    print("All Guitars:")
    for guitar in guitars:
        print(guitar)

def sort_guitars_by_year(guitars):
    """Sort guitars by year (oldest to newest)."""
    guitars.sort()

def add_new_guitar(guitars):
    """Prompt user to enter details of a new guitar and add it to the list."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of manufacture: "))
    cost = float(input("Enter the cost of the guitar: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

def write_guitars_to_file(guitars, filename):
    """Write guitars to a file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)
    display_guitars(guitars)
    sort_guitars_by_year(guitars)
    print("\nSorted Guitars by Year:")
    display_guitars(guitars)
    add_new_guitar(guitars)
    write_guitars_to_file(guitars, filename)
    print("\nNew guitar added and written to file.")

if __name__ == "__main__":
    main()
