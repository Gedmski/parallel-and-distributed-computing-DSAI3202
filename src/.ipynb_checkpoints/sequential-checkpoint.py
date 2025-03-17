from src.functions import square
import time

def sequential_processing(numbers):
    """
    Computes the square of each number in the list sequentially.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    [square(n) for n in numbers]
    end = time.time()
    elapsed_time = end - start
    print(f"Sequential processing time: {elapsed_time:.4f} seconds")
    return elapsed_time