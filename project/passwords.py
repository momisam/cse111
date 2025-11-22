# passwords.py

# ===============================
# Character lists (given by Sven)
# ===============================
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?",
           "/", "`", "~"]


# ===============================
# Function: word_in_file
# ===============================
def word_in_file(word, filename, case_sensitive=False):
    """Check if the word is inside the given file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()  # remove new line
                if case_sensitive:
                    if line == word:
                        return True
                else:
                    if line.lower() == word.lower():
                        return True
    except FileNotFoundError:
        print("File not found:", filename)
    return False


# ===============================
# Function: word_has_character
# ===============================
def word_has_character(word, character_list):
    """Check if the word has any character from the given list."""
    for letter in word:
        if letter in character_list:
            return True
    return False


# ===============================
# Function: word_complexity
# ===============================
def word_complexity(word):
    """Count how many kinds of characters the word has."""
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


# ===============================
# Function: password_strength
# ===============================
def password_strength(password, min_length=10, strong_length=16):
    """Check password strength and return a score (0–5)."""

    # Check dictionary words
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Check top passwords
    if word_in_file(password, "topPasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Check minimum length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Check if it’s very long
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity. This is a good password.")
        return 5

    # Check complexity
    complexity = word_complexity(password)
    strength = 1 + complexity
    print("Password complexity score:", complexity)

    return strength


# ===============================
# Function: main
# ===============================
def main():
    """Main program loop."""
    print("Welcome to the Password Strength Checker!")
    print("Enter 'q' or 'Q' to quit.\n")

    while True:
        password = input("Enter a password: ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        score = password_strength(password)
        print("Password strength score:", score)
        print()  # empty line for spacing


# ===============================
# Run the program
# ===============================
if __name__ == "__main__":
    main()
