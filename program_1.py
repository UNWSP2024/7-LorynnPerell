# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def rainfall_program():
    rainfall = []

    for i in range(1,13):
        while True:
            try:
                amount = float(input(f"Enter rainfall for month [i]: "))
                if amount < 0:
                    raise ValueError("rainfall cant be negative.")
                rainfall.append(amount)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    month_names = {"January", "Febuary", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"}

    max_month = month_names[rainfall.index(max_rainfall)]
    min_month = month_names[rainfall.index(min_rainfall)]

    print("\n--- Rainfall Summary ---")
    print(f"Total Rainfall: {total_rainfall:.2f}")
    print(f"Average Monthly Rainfall: {average_rainfall:.2f}")
    print(f"Highest Rainfall: {max_rainfall:.2f} in {max_month}")
    print(f"Lowest Rainfall: {min_rainfall:.2f} in {min_month}")

    