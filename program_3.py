# Program #3: US_Population

def main():
    all_entered_values = []

    print("Enter population data. Type 'done' as the state name to finish.")

    while True:
        try:
            year = int(input("Enter year: "))
            state = input("Enter state name (or 'done' to finish): ")
            if state.lower() == 'done':
                break
            population = int(input("Enter population: "))
            all_entered_values.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter numbers for year and population.")

    if not all_entered_values:
        print("No data entered.")
        return

    try:
        year_to_sum = int(input("Enter a year to calculate total population for: "))
        sum_population_for_year(all_entered_values, year_to_sum)
    except ValueError:
        print("Invalid year entered.")


def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0
    for entry in all_entered_values:
        year, state, population = entry
        if year == year_to_sum:
            total += population

    print(f"Total population for year {year_to_sum}: {total}")


# Call the main function.
if __name__ == '__main__':
    main()


# Call the main function.
if __name__ == '__main__':
    main()