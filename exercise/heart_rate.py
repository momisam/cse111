"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = int(input("What is your age:  "))
heart_rate = 220 - age
heart_min = int((65 * heart_rate) / 100)
heart_max = int((85 * heart_rate) / 100)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {heart_min} and {heart_max} beats per minute.")