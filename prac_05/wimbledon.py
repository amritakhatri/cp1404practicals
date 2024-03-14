def read_data(filename):
    """Reads data from the given file and returns a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(",") for line in in_file]


def get_champions(data):
    """Returns a dictionary with champions and their number of wins."""
    champions = {}
    for row in data:
        champion = row[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def get_countries(data):
    """Returns a set of countries of champions."""
    return sorted(set(row[1] for row in data) | set(row[3] for row in data))


def main():
    data = read_data("wimbledon_champions.csv")
    champions = get_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
