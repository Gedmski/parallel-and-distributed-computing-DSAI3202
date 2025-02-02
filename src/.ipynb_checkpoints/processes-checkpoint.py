import multiprocessing
import time
import src.functions as f

def testing(chars, n_chunks):
    total_start_time = time.time()
    
    chunk = chars // n_chunks
    # Create processes for both functions
    for i in range(n_chunks):
        process_letters = multiprocessing.Process(target=f.join_random_letters, args=(chunk,))
        process_numbers = multiprocessing.Process(target=f.add_random_numbers, args=(chunk,))

    # Start the processes
        process_letters.start()
        process_numbers.start()

    # Wait for all processes to complete
        process_letters.join()
        process_numbers.join()

    total_end_time = time.time()
    print("----- Processes Results -----")
    print(f"Total time taken: {total_end_time - total_start_time} seconds")
    return total_end_time - total_start_time