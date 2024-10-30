def check_even_odd(number):
    """Determines if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    """Main function to run the program."""
    try:
        # Ask the user for a number
        user_input = int(input("Please enter a number: "))
        # Call the function and get the message
        result_message = check_even_odd(user_input)
        # Print the message
        print(result_message)
    except ValueError:
        print("That's not a valid number. Please enter an integer.")

if __name__ == "__main__":
    main()