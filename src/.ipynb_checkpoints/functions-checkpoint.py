import random
import string

# def join_random_letters(n):
#     letters = [random.choice(string.ascii_letters) for _ in range(n)]
#     joined_letters = ''.join(letters)
#     return joined_letters

# Function to take the sum of a range of numbers
def add_random_numbers(n_start, n_end, queue=None):
    numbers = [_ for _ in range(n_start, n_end)]
    total_sum = sum(numbers)
    print(f"The sum for range ({n_start}, {n_end}) is {total_sum}")
    if queue == None:
        return total_sum
    else:
        queue.put(total_sum)