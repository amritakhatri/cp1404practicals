def main():
    """Display income report for incomes over a given number of months."""
    income_list = []
    num_of_months = int(input("How many months? "))

    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        income_list.append(income)

    print_income_report(num_of_months, income_list)


def print_income_report(num_of_months, income_list):
    """Print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = income_list[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
