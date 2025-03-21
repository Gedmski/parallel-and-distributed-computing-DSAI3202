import random
import string

# def join_random_letters(n):
#     letters = [random.choice(string.ascii_letters) for _ in range(n)]
#     joined_letters = ''.join(letters)
#     return joined_letters

# Function to take the sum of a range of numbers
def add_random_numbers(n_start, n_end, queue=None):
    """
    Computes the sum of integers within a specified range and optionally 
    stores the result in a multiprocessing queue.

    Parameters:
    - n_start (int): The starting number (inclusive) of the range.
    - n_end (int): The ending number (exclusive) of the range.
    - queue (multiprocessing.Queue, optional): If provided, the result is
      placed into this queue instead of returned.

    Returns:
    - int: The sum of numbers in the given range if no queue is provided.
    - None: If a queue is provided, the sum is put into the queue.
    
    Side Effects:
    - Prints the sum for the specified range.
    """
    numbers = [_ for _ in range(n_start, n_end)]
    total_sum = sum(numbers)
    print(f"The sum for range ({n_start}, {n_end}) is {total_sum}")
    if queue == None:
        return total_sum
    else:
        queue.put(total_sum)