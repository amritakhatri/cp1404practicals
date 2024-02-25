def main():
    num_items = get_valid_num_items()
    item_prices = [float(input(f"Price of item {i + 1}: ")) for i in range(num_items)]

    total_price = calculate_total_price(num_items, item_prices)

    print(f"Total price for {num_items} items is ${total_price:.2f}")

def calculate_total_price(num_items, item_prices):
    total_price = sum(item_prices)
    return total_price * 0.9 if total_price > 100 else total_price


def get_valid_num_items():
    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items >= 0:
                return num_items
            else:
                print("Invalid number of items!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()