import multiprocessing
import time
from math import ceil
from multiprocessing import Queue
import src.functions as f

def testing(chars, n_chunks):
    partial_sums = Queue()
    
    total_start_time = time.time()
    
    chunk = ceil(chars / n_chunks)
    # Create processes for both functions
    processes = []
    for i in range(n_chunks):
        # process_letters = multiprocessing.Process(target=f.join_random_letters, args=(chunk,))
        process_numbers = multiprocessing.Process(target=f.add_random_numbers, args=(chunk*i, min(chunk*(i+1), chars + 1), partial_sums))
        # processes.append(process_letters)
        processes.append(process_numbers)
        # process_letters.start()
        process_numbers.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    
    total = 0
    while not partial_sums.empty():
        partial_sum = partial_sums.get()
        total += partial_sum

    print(f"The sum for range ({0}, {chars}) is {total}")
    
    total_end_time = time.time()
    print("----- Processes Results -----")
    print(f"Total time taken: {total_end_time - total_start_time} seconds")
    print("------------------------------------------------------------------")
    return total_end_time - total_start_time