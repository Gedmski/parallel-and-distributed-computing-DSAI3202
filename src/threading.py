import threading
import time
from math import ceil
from queue import Queue
import src.functions as f

def testing(chars, n_chunks):
    partial_sums = Queue()
    
    total_start_time = time.time()

    chunk = ceil(chars / n_chunks)
    # Create threads for both functions
    threads = []
    for i in range(n_chunks):
        # thread_letters = threading.Thread(target=f.join_random_letters, args=(chunk,))
        thread_numbers = threading.Thread(target=f.add_random_numbers, args=(chunk*i, min(chunk*(i+1), chars + 1), partial_sums))
        # threads.append(thread_letters)
        threads.append(thread_numbers)
        # thread_letters.start()
        thread_numbers.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    total = 0
    while not partial_sums.empty():
        partial_sum = partial_sums.get()
        total += partial_sum

    print(f"The sum for range ({0}, {chars}) is {total}")
    
    total_end_time = time.time()
    print("----- Threading Results -----")
    print(f"Total time taken: {total_end_time - total_start_time} seconds")
    print("------------------------------------------------------------------")
    return total_end_time - total_start_time