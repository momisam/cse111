def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")

  # Add code to reverse and print fruit_list.
  rev_fruit = fruit_list[::-1]
  print(f"reversed: {rev_fruit}")

  # Add code to append "orange" to the end of fruit_list and print the list.
  fruit_list.append("orange")
  print(f"append orange: {fruit_list}")

  # Add code to find where "apple" is located and insert "cherry" before it.
  apple_index = fruit_list.index("apple")
  fruit_list.insert(apple_index, "cherry")
  print(f"insert 'cherry': {fruit_list}")

  # Add code to remove "banana" from fruit_list and print the list.
  fruit_list.remove("banana")
  print(f"remove 'banana': {fruit_list}")

  # Add code to pop the last element and print the popped element and the list.
  popped = fruit_list.pop()
  print(f"popped element: {popped}")
  print(f"after pop: {fruit_list}")

  # Add code to sort and print fruit_list.
  fruit_list.sort()
  print(f"sorted: {fruit_list}")

  # Add code to clear and print fruit_list.
  fruit_list.clear()
  print(f"cleared: {fruit_list}")


if __name__ == "__main__":
  main()
