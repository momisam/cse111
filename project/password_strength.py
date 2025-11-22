# passwords.py
# W02 Project: Password Strength Checker
# Programmer: [Your Name]
# Enhancement: Added feedback suggestions after each password check to help users improve their passwords.

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?",
           "/", "`", "~"]


def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if case_sensitive:
                    if word == line:
                        return True
                else:
                    if word.lower() == line.lower():
                        return True
    except FileNotFoundError:
        print("File not found:", filename)
    return False


def word_has_character(word, character_list):
    for letter in word:
        if letter in character_list:
            return True
    return False


def word_complexity(word):
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


def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "topPasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity. This is a good password.")
        return 5

    complexity = word_complexity(password)
    strength = 1 + complexity
    print("Password complexity score:", complexity)
    return strength


def main():
    print("===========================================")
    print("Welcome to the Password Strength Checker!")
    print("Type 'q' or 'Q' anytime to quit.")
    print("===========================================")

    while True:
        password = input("Enter a password to test: ")
        if password.lower() == "q":
            print("Thank you for using the Password Checker. Goodbye!")
            break
        score = password_strength(password)
        print(f"Password strength score: {score}/5")
        if score <= 1:
            print("→ Try adding more characters, numbers, or symbols.")
        elif score == 2 or score == 3:
            print("→ Better! Add uppercase or symbols to make it stronger.")
        elif score == 4:
            print("→ Great password! Just a bit longer would make it perfect.")
        elif score == 5:
            print("→ Excellent! This password is strong and secure.")


if __name__ == "__main__":
    main()
