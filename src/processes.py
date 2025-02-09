import multiprocessing
import time
import src.functions as f

def testing(chars, n_chunks):
    total_start_time = time.time()
    
    chunk = chars // n_chunks
    # Create processes for both functions
    processes = []
    for i in range(n_chunks):
        # process_letters = multiprocessing.Process(target=f.join_random_letters, args=(chunk,))
        process_numbers = multiprocessing.Process(target=f.add_random_numbers, args=(chunk*i, chunk*(i+1)))
        # processes.append(process_letters)
        processes.append(process_numbers)
        # process_letters.start()
        process_numbers.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    total_end_time = time.time()
    print("----- Processes Results -----")
    print(f"Total time taken: {total_end_time - total_start_time} seconds")
    print("------------------------------------------------------------------")
    return total_end_time - total_start_time