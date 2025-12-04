# Enhancement Added:
# This program prints how many days remain until New Year's Day (January 1).
# This enhancement fulfills the extra creativity requirement for full credit.

import csv
import datetime


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a dictionary and return it.
    The key for each dictionary item is found in the column indicated
    by key_column_index. The value is the entire row from the CSV file.
    """
    dictionary = {}

    try:
        with open(filename, "r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip header row

            for row in reader:
                if len(row) != 0:
                    key = row[key_column_index]
                    dictionary[key] = row

    except FileNotFoundError as err:
        print("Error: missing file")
        print(err)
        exit()

    except PermissionError as err:
        print("Error: permission denied")
        print(err)
        exit()

    return dictionary


def main():
    try:
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        with open("request.csv", "r", newline="") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # skip header

            number_of_items = 0
            subtotal = 0

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                # Lookup — may raise KeyError
                product_info = products_dict[product_id]

                product_name = product_info[1]
                price = float(product_info[2])

                print(f"{product_name}: {quantity} @ {price:.2f}")

                number_of_items += quantity
                subtotal += price * quantity

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Number of Items: {number_of_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")

        # Print current date/time
        current_time = datetime.datetime.now()
        print(current_time.strftime("%a %b %d %H:%M:%S %Y"))

        # ⭐ Enhancement: Days until New Year
        new_year = datetime.datetime(current_time.year + 1, 1, 1)
        days_left = (new_year - current_time).days
        print(f"Days until New Year's sale: {days_left}")

    except KeyError as err:
        print("Error: unknown product ID in the request.csv file")
        print(err)

    except FileNotFoundError as err:
        print("Error: missing file")
        print(err)

    except PermissionError as err:
        print("Error: permission denied")
        print(err)


if __name__ == "__main__":
    main()
