import random
import string

def generate(length, use_upper, use_digit, use_symbol):
    # base password
    pass1 = string.ascii_lowercase

    # Add other character
    if use_upper:
        pass1 += string.ascii_uppercase
    if use_digit:
        pass1 += string.digits
    if use_symbol:
        pass1 += string.punctuation

    # Check if empty
    if not pass1:
        return "Error: Please select at least one character type."

    password_list = random.choices(pass1, k=length)

    return "".join(password_list)

def main():
    print("🔑 Random Password Generator")
    print("---------------------------")

    try:
        length=int(input("Enter desired password length : "))
        if length<=0:
            print("Password length must be a positive number.")
            return

        use_upper = input("Use uppercase letters? (y/n): ").lower() == 'y'
        use_digit = input("Use digits? (y/n): ").lower() == 'y'
        use_symbol = input("Use symbols? (y/n): ").lower() == 'y'

        password=generate(length,use_upper, use_digit, use_symbol)

        print("\n---------------------------")
        print(f"✅ Generated Password: {password}")
        print("---------------------------")

    except ValueError:
        print("Invalid input. Please enter valid number for length.")


if __name__ == "__main__":
    main()