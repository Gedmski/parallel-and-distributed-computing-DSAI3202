import random
import string

def join_random_letters(n):
    """
    Generates a string composed of 'n' random ASCII letters (both uppercase and lowercase).

    Parameters:
    - n (int): The number of random letters to generate.

    Returns:
    - str: A string of randomly chosen ASCII letters.
    """
    letters = [random.choice(string.ascii_letters) for _ in range(n)]
    joined_letters = ''.join(letters)
    return joined_letters

# Function to add a thousand random numbers
def add_random_numbers(n):
    """
    Generates 'n' random integers between 1 and 100 and returns their sum.

    Parameters:
    - n (int): The number of random integers to generate and sum.

    Returns:
    - int: The sum of the randomly generated integers.
    """
    numbers = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(numbers)
    return total_sum