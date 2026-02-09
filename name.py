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


# TASK
