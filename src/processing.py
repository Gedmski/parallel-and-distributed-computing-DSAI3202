from src.functions import square
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

def multiprocessing_for_loop(numbers):
    start = time.time()
    processes = []
    for n in numbers:
        p = multiprocessing.Process(target=square, args=(n,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    end = time.time()
    elapsed_time = end - start
    print(f"Multiprocessing for loop time: {elapsed_time:.4f} seconds")
    return elapsed_time


def multiprocessing_pool_apply_sync(numbers):
    """
    Uses multiprocessing Pool with apply() in a synchronous manner.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = [pool.apply(square, args=(n,)) for n in numbers]  # Synchronous execution
    end = time.time()
    elapsed_time = end - start
    print(f"Synchronous Pool (apply) time: {elapsed_time:.4f} seconds")
    return elapsed_time

def multiprocessing_pool_map_sync(numbers):
    """
    Uses multiprocessing Pool with map() in a synchronous manner.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)  # Synchronous execution
    end = time.time()
    elapsed_time = end - start
    print(f"Synchronous Pool (map) time: {elapsed_time:.4f} seconds")
    return elapsed_time

def multiprocessing_pool_apply_async(numbers):
    """
    Uses multiprocessing Pool with apply_async() in an asynchronous manner.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = [pool.apply_async(square, args=(n,)) for n in numbers]  # Asynchronous execution
        [r.get() for r in results]  # Ensures completion
    end = time.time()
    elapsed_time = end - start
    print(f"Asynchronous Pool (apply_async) time: {elapsed_time:.4f} seconds")
    return elapsed_time

def multiprocessing_pool_map_async(numbers):
    """
    Uses multiprocessing Pool with map_async() in an asynchronous manner.
    
    Args:
        numbers (list): List of numbers to be squared.
    
    Returns:
        float: The elapsed time of execution.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map_async(square, numbers)  # Asynchronous execution
        result.wait()  # Wait for completion
    end = time.time()
    elapsed_time = end - start
    print(f"Asynchronous Pool (map_async) time: {elapsed_time:.4f} seconds")
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