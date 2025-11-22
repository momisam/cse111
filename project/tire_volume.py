# Step 1: Import required modules
from datetime import datetime   # for current date
import math                     # for math.pi

# Step 2: Ask user for tire details
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Step 3: Calculate tire volume
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Step 4: Display result with two decimal places
print(f"The approximate volume is {volume:.2f} liters")

# Step 5: Get current date (no time)
current_date_and_time = datetime.now()
current_date = f"{current_date_and_time:%Y-%m-%d}"

# Step 6: Append details to volumes.txt
with open("volumes.txt", "at") as file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=file)

# Enhancement: Ask if user wants to buy tires and save phone number
buy = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()
if buy == "yes" or "y":
    phone = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as file:
        print(f"Customer interest - Phone: {phone}", file=file)
    print("Your interest has been recorded. Thank you!")

