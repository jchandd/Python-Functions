# Username Creator


# This script asks the User for name
# It will format name and chack if age is valid
# Then, it will print message onto screen


def format_username(name: str) -> str:

    # Formats a name into a simple username

    # Clean up name (remove extra space)
    clean_name = name.strip()

    # Convert name to lowercase
    clean_name = clean_name.lower()

    # Replace space with underscores
    username = clean_name.replace(" ", "_")

    # Return completed username
    return username


def get_age() -> int:

    # Ask the user for age and validate input.

    # TRY to get and convert user input to integer
    try:
        # Ask user for age
        age_input = input("Enter your age: ")

        # Convert input to integer
        age = int(age_input)

        # Return valid age
        return age

    # If conversion fails or age invalid...
    except ValueError:
        # Print nice message
        print("Invalid age entered.")

        # Return -1 to signal an error
        return -1


def main() -> None:

    # Main program logic.

    # Ask user for their full name
    name = input("Enter your full name: ")

    # Call format_username to create username
    username = format_username(name)

    # Call get_age to get valid age
    age = get_age()

    # If age is valid
    if age != -1:
        print(f"Welcome, {username}! Your are {age} years old")

    # If age not valid
    else:
        print("Please restart the program and try again.")


# Run the main function
if (
    __name__ == "__functions__"
):  # Makes sure the code doesn't run if imported by someone
    main()
