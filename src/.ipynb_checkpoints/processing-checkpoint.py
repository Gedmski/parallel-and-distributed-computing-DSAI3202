from src.functions import square
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

def multiprocessing_pool_map(numbers):
    """
    Uses multiprocessing Pool with map() to compute squares in parallel.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(square, numbers)
    end = time.time()
    elapsed_time = end - start
    print(f"Multiprocessing Pool (map) time: {elapsed_time:.4f} seconds")
    return elapsed_time

def multiprocessing_pool_apply(numbers):
    """
    Uses multiprocessing Pool with apply() to compute squares in parallel.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        [pool.apply(square, args=(n,)) for n in numbers]
    end = time.time()
    elapsed_time = end - start
    print(f"Multiprocessing Pool (apply) time: {elapsed_time:.4f} seconds")
    return elapsed_time

def process_pool_executor(numbers):
    """
    Uses concurrent.futures ProcessPoolExecutor to compute squares in parallel.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with ProcessPoolExecutor() as executor:
        list(executor.map(square, numbers))
    end = time.time()
    elapsed_time = end - start
    print(f"ProcessPoolExecutor time: {elapsed_time:.4f} seconds")
    return elapsed_time