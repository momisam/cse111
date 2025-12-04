import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Reads the CSV into a dictionary using the key column."""
    dictionary = {}

    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)          # skip header

        for row in reader:
            if len(row) == 0:
                continue

            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


def main():
    try:
        # ------------------------------
        # 1. Read product catalog
        # ------------------------------
        products_dict = read_dictionary("products.csv", 0)

        # ------------------------------
        # 2. Open request.csv
        # ------------------------------
        with open("request.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)                 # skip header

            print("My Grocery Store")    # store name
            print()

            total_items = 0
            subtotal = 0

            # ------------------------------
            # 3. Process each requested item
            # ------------------------------
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                # This will raise KeyError if product is unknown
                product_info = products_dict[product_number]

                product_name = product_info[1]
                product_price = float(product_info[2])

                line_total = quantity * product_price

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

                total_items += quantity
                subtotal += line_total

            # ------------------------------
            # 4. Totals
            # ------------------------------
            tax = subtotal * 0.06
            total = subtotal + tax

            print()
            print(f"Number of Items: {total_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: {total:.2f}")
            print("Thank you for shopping with us.")

            # ------------------------------
            # 5. Print current date/time
            # ------------------------------
            current_time = datetime.now()
            print(current_time.strftime("%a %b %d %H:%M:%S %Y"))

    # ------------------------------
    # ERROR HANDLING
    # ------------------------------
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

    except PermissionError as e:
        print("Error: permission denied")
        print(e)

    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


# Run main
if __name__ == "__main__":
    main()
