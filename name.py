# TASK: Write function that returns random encourgement messages

import random


def get_encouragement() -> str:
    """Returns random encouraging message"""
    message1 = "You got this!"
    message2 = "Don't stop trying!"
    message3 = "Keep believing in yourself!"
    message4 = "each step counts!"

    random_number = random.randint(1, 4)

    if random_number == 1:
        return message1
    elif random_number == 2:
        return message2
    elif random_number == 3:
        return message3
    else:
        return message4


# Call function and print result
print(get_encouragement())


# TASK: Write fuction to ask for valid age input

def get_valid_age(prompt: str) -> int:
    """Asks the user for valid age input, ensure positive integer"""
    while True:
        try:
            age = int(input(prompt))
            if age > 0:
                return age
            else:
                print("Enter positive number")
            except ValueError:
                print("Invalid input. Please enter number")

# Call function and store results
user_age = get_valid_age("Enter age")

# Display valid age
print(f"Your valid age: {user_age}")


# TASK write function to reverse words and capitalize

def reverse_and_capitalize(word: str) -> str:
    """
    Reverse word and capitalize

    :param word: Input word
    :return: reversed word uppercased
    """

    # Reverse the word
    reversed_word = word[::-1]

    return reversed_word.upper()

# Prompt user to enter word
user_word = input("Enter word: ")

# Call function to store result
reversed_result = reverse_and_capitalize(user_word)

# Display new word
print(f"Reversed and capitalized: {reversed_result}")