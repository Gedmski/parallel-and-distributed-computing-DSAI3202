import random
import string

def join_random_letters(n):
    letters = [random.choice(string.ascii_letters) for _ in range(n)]
    joined_letters = ''.join(letters)
    return joined_letters

# Function to add a thousand random numbers
def add_random_numbers(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(numbers)
    return total_sum