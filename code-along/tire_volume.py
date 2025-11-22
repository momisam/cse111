"""tire_volume.py
This program calculates the approximate volume of air inside a tire based on
the tire’s width, aspect ratio, and wheel diameter. It then logs the data to
a file named volumes.txt.

Enhancements:
- Appends data with the current date to volumes.txt for future analysis.
"""

import math
from datetime import datetime

# Get user input
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute the volume using the given formula:
# v = (π * w^2 * a * (w * a + 2540 * d)) / 10,000,000,000
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000

# Round volume to two decimal places
volume = round(volume, 2)

# Display the result
print(f"The approximate volume is {volume:.2f} liters")

# Get current date (without time)
current_date_and_time = datetime.now()
current_date = f"{current_date_and_time:%Y-%m-%d}"

# Append results to volumes.txt
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}", file=volumes_file)
