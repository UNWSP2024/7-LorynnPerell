# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

rainfall = []

# Input rainfall for each month
for month in months:
    while True:
        try:
            amount = float(input(f"Enter rainfall for {month}: "))
            if amount < 0:
                raise ValueError("Rainfall cannot be negative.")
            rainfall.append(amount)
            break
        except ValueError as e:
            print("Invalid input:", e)

total = sum(rainfall)
average = total / 12
max_rain = max(rainfall)
min_rain = min(rainfall)
max_month = months[rainfall.index(max_rain)]
min_month = months[rainfall.index(min_rain)]

print("\nRainfall Summary:")
print(f"Total rainfall: {total:.2f}")
print(f"Average monthly rainfall: {average:.2f}")
print(f"Highest rainfall in: {max_month} ({max_rain:.2f})")
print(f"Lowest rainfall in: {min_month} ({min_rain:.2f})")