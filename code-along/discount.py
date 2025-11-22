"""You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store’s slowest sales days. 
On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, 
the store will discount the customer’s subtotal by 10%."""
from datetime import date
discount_rate = 0.10 #10% dicount rate
tax_rate = 0.06 #6% tax rate
discount = 0 #dicount if not on the day of discount
subtotal = float(input("Enter the subtotal: $"))
today = date.today() #Get today date from the operating system 
days_of_week = today.weekday() #Return an integer of the day week Monday = 0, Sunday = 6

if (days_of_week == 1 or days_of_week == 2) 
    if subtotal >= 50:
        discount = subtotal * discount_rate
        print(f"Discount Received is: {discount}")
else:
    discount = 0

subtotal -= discount
tax = subtotal * tax_rate

total = subtotal + tax

print(f"Sale Tax: ${tax:.2f}")
print(f"Total Amount Due: ${total:.2f}")


